#!/usr/bin/env python3
# ============================================================
# wiki_auto_sync.py — 多仓库日同步脚本
# Daily Multi-Repository Synchronization Script
#
# Syncs 3 repos to GitHub with automatic user switching via gh CLI.
# 通过 gh CLI 自动切换 GitHub 用户，将 3 个仓库同步到 GitHub。
# ============================================================

import os
import subprocess
from datetime import datetime

# 仓库配置 | Repository Configuration
REPOS = {
    "llm-wiki": {
        "path": "/root/hermes-shared/wiki",
        "user": "joe12803",
        "branch": "master"
    },
    "mining-toolkit": {
        "path": "/root/autonomous-mining-toolkit",
        "user": "joe12801",
        "branch": "main"
    },
    "mining-results": {
        "path": "/root/exploration-mining-results",
        "user": "joe12801",
        "branch": "main"
    }
}

def run_cmd(cmd, cwd=None):
    """Execute shell command | 执行 Shell 命令"""
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)

def switch_gh_user(user):
    """Switch GitHub CLI authenticated user | 切换 GitHub CLI 认证用户"""
    print(f"Switching to GitHub user | 切换到用户: {user}")
    run_cmd(f"gh auth switch --hostname github.com --user {user}")

def sync_all():
    """Sync all configured repos | 同步所有已配置的仓库"""
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = [f"### 📊 Hermes Daily Mining Report | 每日采矿报告 [{today}]"]

    for name, config in REPOS.items():
        path = config["path"]
        user = config["user"]
        branch = config["branch"]

        if not os.path.exists(path):
            report.append(f"- **{name}**: ⚠️ Path not found | 路径不存在: {path}")
            continue

        print(f"Syncing | 同步中: {name}...")
        switch_gh_user(user)

        # Stage all changes | 暂存所有变更
        run_cmd("git add .", cwd=path)
        # Commit | 提交
        res = run_cmd(f'git commit -m "auto: Daily synchronization {today}"', cwd=path)

        if "nothing to commit" in res.stdout:
            report.append(f"- **{name}**: No changes today. | 今日无变更。")
            continue

        # Push to remote | 推送到远程
        push_res = run_cmd(f"git push origin {branch}", cwd=path)

        if push_res.returncode == 0:
            report.append(f"- **{name}**: ✅ Synced successfully | 同步成功")
        else:
            report.append(f"- **{name}**: ❌ Sync failed! | 同步失败! {push_res.stderr[:100]}")

    # Print summary report | 打印汇总报告
    print("\n".join(report))

if __name__ == "__main__":
    sync_all()
