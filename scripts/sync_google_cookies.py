#!/usr/bin/env python3
"""
sync_google_cookies.py
───────────────────────────────────────────────────────────────────
从真实 Chrome（通过 browser-harness CDP）提取 Google 系 Cookie，
合并写入 notebooklm 的 storage_state.json，保持登录态永不过期。

用法：
    python3 sync_google_cookies.py [--dry-run] [--verbose]

依赖：
    browser-harness 已安装且 Chrome 开启远程调试（port 9222）
    即：`browser-harness --doctor` 通过

原理：
    CDP Network.getAllCookies → 过滤 Google 域名 → 合并到 storage_state
"""

import argparse
import json
import os
import shutil
import socket
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

# ── 配置 ──────────────────────────────────────────────────────────
CHROME_DEBUG_PORT = 9222
STORAGE_STATE_PATH = Path.home() / ".notebooklm/profiles/default/storage_state.json"
BACKUP_DIR = Path.home() / ".notebooklm/profiles/default/cookie_backups"

# 需要同步的域名（notebooklm 需要这些 Google Cookie）
TARGET_DOMAINS = {
    ".google.com",
    "google.com",
    "accounts.google.com",
    "notebooklm.google.com",
    "myaccount.google.com",
    "workspace.google.com",
}

# ── CDP 通信 ──────────────────────────────────────────────────────
def get_chrome_ws_url(port: int = CHROME_DEBUG_PORT) -> str:
    """从 Chrome /json/version 获取 WebSocket 调试地址"""
    try:
        url = f"http://127.0.0.1:{port}/json/version"
        with urllib.request.urlopen(url, timeout=5) as resp:
            data = json.loads(resp.read())
            return data["webSocketDebuggerUrl"]
    except Exception as e:
        raise RuntimeError(
            f"无法连接 Chrome 调试接口（port {port}）: {e}\n"
            f"请确保 Chrome 以 --remote-debugging-port={port} 启动，\n"
            f"或运行 `browser-harness --doctor` 检查状态。"
        )


def cdp_call(ws_url: str, method: str, params: dict = None) -> dict:
    """发送 CDP 命令，返回 result 字段"""
    import threading
    import json as _json

    # 用 websocket-client 或 fallback 到 raw socket
    try:
        import websocket  # websocket-client
        ws = websocket.create_connection(ws_url, timeout=10)
        ws.send(_json.dumps({"id": 1, "method": method, "params": params or {}}))
        raw = ws.recv()
        ws.close()
        resp = _json.loads(raw)
        if "error" in resp:
            raise RuntimeError(f"CDP error: {resp['error']}")
        return resp.get("result", {})
    except ImportError:
        pass

    # fallback：通过 browser-harness IPC（如果已启动 daemon）
    # 找 Unix socket 路径
    bu_name = os.environ.get("BU_NAME", "default")
    sock_path = f"/tmp/bu-{bu_name}.sock"
    if not Path(sock_path).exists():
        raise RuntimeError(
            "websocket-client 未安装，且 browser-harness daemon 未运行。\n"
            "请运行：pip install websocket-client\n"
            "或先启动 daemon：browser-harness --doctor"
        )

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(sock_path)
        req = _json.dumps({"method": method, "params": params or {}}) + "\n"
        s.sendall(req.encode())
        buf = b""
        while True:
            chunk = s.recv(65536)
            if not chunk:
                break
            buf += chunk
            try:
                resp = _json.loads(buf.decode())
                break
            except _json.JSONDecodeError:
                continue
    if "error" in resp:
        raise RuntimeError(f"CDP error: {resp['error']}")
    return resp.get("result", {})


# ── Cookie 处理 ───────────────────────────────────────────────────
def get_page_session_id(ws_url: str) -> str | None:
    """
    从 browser-level target 获取第一个可用页面的 sessionId，
    用于发送需要 page context 的 CDP 命令（如 Network.getAllCookies）。
    """
    import json as _json
    import websocket

    # 1. 先通过 /json/list 获取页面列表
    port = int(ws_url.split(":")[2].split("/")[0])
    url = f"http://127.0.0.1:{port}/json/list"
    with urllib.request.urlopen(url, timeout=5) as resp:
        targets = json.loads(resp.read())

    # 找第一个 page 类型 target
    page_targets = [t for t in targets if t.get("type") == "page"]
    if not page_targets:
        return None, None

    target = page_targets[0]
    target_id = target["id"]
    ws_page_url = target["webSocketDebuggerUrl"]
    return target_id, ws_page_url


def fetch_google_cookies(ws_url: str, verbose: bool = False) -> list[dict]:
    """从 Chrome 提取所有 Google 域名的 Cookie（通过页面级 CDP session）"""
    # Network.getAllCookies 需要在 page target 上调用
    target_id, ws_page_url = get_page_session_id(ws_url)
    if not ws_page_url:
        raise RuntimeError("找不到可用的页面 target，Chrome 中没有打开的标签页")
    if verbose:
        print(f"  使用页面 target: {ws_page_url}")

    result = cdp_call(ws_page_url, "Network.getAllCookies")
    all_cookies = result.get("cookies", [])

    google_cookies = [
        c for c in all_cookies
        if any(
            c.get("domain", "").endswith(d.lstrip(".")) or
            c.get("domain", "") == d
            for d in TARGET_DOMAINS
        )
    ]

    if verbose:
        print(f"  Chrome 总 Cookie 数: {len(all_cookies)}")
        print(f"  Google 域名 Cookie 数: {len(google_cookies)}")
        domains = sorted({c["domain"] for c in google_cookies})
        print(f"  涉及域名: {', '.join(domains)}")

    return google_cookies


def normalize_cookie(c: dict) -> dict:
    """将 CDP cookie 格式标准化为 Playwright storage_state 格式"""
    normalized = {
        "name": c["name"],
        "value": c["value"],
        "domain": c["domain"],
        "path": c.get("path", "/"),
        "expires": c.get("expires", -1),
        "httpOnly": c.get("httpOnly", False),
        "secure": c.get("secure", False),
        "sameSite": c.get("sameSite", "Lax"),
    }
    # CDP 有时用 session=True 表示会话 cookie（expires=-1）
    if c.get("session", False):
        normalized["expires"] = -1
    return normalized


def merge_cookies(existing: list[dict], fresh: list[dict]) -> tuple[list[dict], int, int]:
    """
    将 fresh cookies 合并进 existing，以 (name, domain, path) 为唯一键。
    返回 (merged_list, updated_count, added_count)
    """
    # 构建现有 cookie 索引
    index = {
        (c["name"], c["domain"], c.get("path", "/")): i
        for i, c in enumerate(existing)
    }

    result = list(existing)
    updated = 0
    added = 0

    for fc in fresh:
        key = (fc["name"], fc["domain"], fc.get("path", "/"))
        if key in index:
            old = result[index[key]]
            if old["value"] != fc["value"] or old.get("expires") != fc.get("expires"):
                result[index[key]] = fc
                updated += 1
        else:
            result.append(fc)
            index[key] = len(result) - 1
            added += 1

    return result, updated, added


# ── 主流程 ────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="同步 Google Cookie 到 notebooklm storage_state")
    parser.add_argument("--dry-run", action="store_true", help="只显示将要做的事，不实际写入")
    parser.add_argument("--verbose", "-v", action="store_true", help="显示详细信息")
    parser.add_argument("--port", type=int, default=CHROME_DEBUG_PORT, help=f"Chrome 调试端口（默认 {CHROME_DEBUG_PORT}）")
    parser.add_argument("--output", type=Path, default=STORAGE_STATE_PATH, help="storage_state.json 路径")
    args = parser.parse_args()

    print(f"🔍 连接 Chrome（port {args.port}）...")
    ws_url = get_chrome_ws_url(args.port)
    if args.verbose:
        print(f"  WebSocket URL: {ws_url}")

    print("🍪 提取 Google Cookie...")
    fresh_cookies_raw = fetch_google_cookies(ws_url, verbose=args.verbose)
    fresh_cookies = [normalize_cookie(c) for c in fresh_cookies_raw]

    print(f"📂 读取 storage_state: {args.output}")
    if not args.output.exists():
        print("  ⚠️  文件不存在，将创建新文件")
        existing_state = {"cookies": [], "origins": []}
    else:
        with open(args.output) as f:
            existing_state = json.load(f)

    existing_cookies = existing_state.get("cookies", [])
    print(f"  现有 Cookie 数: {len(existing_cookies)}")

    merged, updated, added = merge_cookies(existing_cookies, fresh_cookies)
    print(f"✅ 合并结果: 更新 {updated} 个 · 新增 {added} 个 · 总计 {len(merged)} 个")

    if updated == 0 and added == 0:
        print("🟰 Cookie 无变化，无需更新")
        return

    if args.dry_run:
        print("🚫 Dry-run 模式，跳过写入")
        if args.verbose:
            print("\n将要更新的 Cookie：")
            for c in fresh_cookies:
                print(f"  {c['domain']} | {c['name']} | expires={c['expires']}")
        return

    # 备份原文件
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"storage_state_{ts}.json"
    shutil.copy2(args.output, backup_path)
    print(f"💾 已备份原文件: {backup_path}")

    # 写入新文件
    new_state = dict(existing_state)
    new_state["cookies"] = merged
    with open(args.output, "w") as f:
        json.dump(new_state, f, indent=2, ensure_ascii=False)

    print(f"✅ 已写入: {args.output}")
    print(f"🕐 同步时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
