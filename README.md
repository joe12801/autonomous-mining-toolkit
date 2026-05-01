# ⛏️ Autonomous Mining Toolkit v3.0

> **Industrial-grade AI knowledge extraction pipeline.**  
> **AI 驱动的知识提取工业化生产线 (SOP v3.0)**

将任意 GitHub 仓库转化为结构化知识资产：飞书文档 + Obsidian 笔记 + NotebookLM 深度分析 + 代码图谱可视化。

---

## 📋 7-Phase SOP | 七阶段标准作业流程

| Phase | 名称 | 工具 | 产出 |
|-------|------|------|------|
| **1** | Metadata 元数据 | GitHub API | 仓库基本信息 |
| **2** | Drilling 钻探 | `driller.py` | 源码矿包 `.txt` |
| **3** | Graphify 图谱 | `graphify` | `graph.html` + `GRAPH_REPORT.md` + 上传飞书云盘 |
| **4** | Mining 开采 | NotebookLM CLI | 深度分析报告 |
| **5** | Feishu Doc 飞书文档 | `lark-cli` | 飞书文档链接 |
| **6** | Sync 同步 | — | 发送链接给用户 |
| **7** | Obsidian *(可选)* | rclone + Google Drive | Obsidian vault 笔记 |

---

## 🛠️ 核心组件

### 1. 🚰 driller.py — 源码精炼

将仓库源码提取为高密度矿包，自动过滤 `node_modules`、二进制文件等噪声，支持自动分片。

```bash
python3 scripts/driller.py <仓库路径> <输出前缀>
# 产出: <输出前缀>_part1.txt, _part2.txt, ...
```

**示例：**
```bash
mkdir -p /tmp/mining/my-repo
chown -R joe1280 /tmp/mining/my-repo
sudo -u joe1280 python3 scripts/driller.py ./my-repo /tmp/mining/my-repo/ore
```

---

### 2. 🗺️ graphify — 代码图谱

静态分析代码结构，构建模块依赖图谱，识别核心节点（God Nodes）。

```bash
python3 scripts/graphify update <仓库路径>
# 产出: <仓库路径>/graphify-out/graph.html, graph.json, GRAPH_REPORT.md
```

`graph.html` 是自包含的交互式网页，可本地浏览器打开，支持节点拖拽、社区过滤。

**上传到飞书云盘：**
```bash
cd <仓库路径>/graphify-out
lark drive +upload --file ./graph.html
# 返回 file_token，可作为附件发送给用户
```

---

### 3. 📒 NotebookLM CLI — 深度开采

利用 Google NotebookLM 的超长上下文对矿包进行语义挖掘。

```bash
# 创建笔记本（保存完整 UUID）
sudo -u joe1280 notebooklm create "<项目名> 深度开采报告"
# → Created notebook: <full-uuid> - <title>

# 切换上下文（必须在 source add 之前）
sudo -u joe1280 notebooklm use <full-uuid>

# 添加矿包（必须用 --type file）
cp /path/to/ore_part1.txt /tmp/ore.txt
chown joe1280 /tmp/ore.txt
sudo -u joe1280 notebooklm source add /tmp/ore.txt \
    --type file --mime-type "text/plain" --title "<项目> 完整源码"

# 添加图谱报告（可选）
sudo -u joe1280 notebooklm source add /tmp/graph_report.md \
    --type file --mime-type "text/plain" --title "<项目> 代码图谱"

# 添加 GitHub URL（可选）
sudo -u joe1280 notebooklm source add https://github.com/<owner>/<repo>

# 深度提问
sudo -u joe1280 notebooklm ask "请详细分析架构、核心模块、设计哲学..."
```

**⚠️ 关键陷阱：**
- `source add` 必须用 `--type file --mime-type "text/plain"`，用 `--type text` 或自动检测会把文件路径当内容
- `notebooklm list` 显示的 ID 是截断的，**务必从 `create` 输出保存完整 UUID**
- `source add` 前必须先 `notebooklm use <uuid>` 设置上下文

---

### 4. 📄 lark-cli — 飞书文档发布

```bash
sudo -u joe1280 bash -c "cat report.md | lark docs +create --title '<项目> 开采报告' --markdown -"
# 返回 doc_url: https://www.feishu.cn/docx/...
```

**⚠️ 注意：** 命令是 `lark docs +create`（有 `+`），不是 `lark docs create`。

---

### 5. 🔄 keep_alive_notebooklm.sh — Session 保活

保持 NotebookLM Google Session 活跃，防止 Cookie 过期。

```bash
bash scripts/keep_alive_notebooklm.sh
```

建议配置定时任务每 30 分钟运行一次。

---

### 6. 🗒️ Obsidian + Google Drive 同步（可选 Phase 7）

挖矿报告写入本地 Obsidian vault，通过 rclone 自动同步到 Google Drive，在 Windows Obsidian 中查看。

**本地 vault：** `/home/joe1280/obsidian-vault/`  
**Google Drive：** `gdrive:ObsidianVault/`

```bash
# 手动同步
rclone sync /home/joe1280/obsidian-vault gdrive:ObsidianVault

# 写入挖矿报告（标准格式）
VAULT="/home/joe1280/obsidian-vault"
mkdir -p "$VAULT/Mining"
cat > "$VAULT/Mining/<repo-name>.md" << 'EOF'
---
tags: [mining, github, <language>]
repo: https://github.com/<owner>/<repo>
stars: <N>
date: <YYYY-MM-DD>
feishu: <feishu_doc_url>
---

# <repo-name> 深度开采报告

[[Mining/Index]]

<报告内容>
EOF
```

---

## 🚀 快速开始

### 环境要求

| 依赖 | 版本 | 用途 |
|------|------|------|
| Python | 3.10+ | driller.py, graphify |
| notebooklm-py | latest | NotebookLM CLI |
| lark-cli | 1.0.14+ | 飞书文档发布 |
| rclone | 1.60+ | Google Drive 同步 |

### 一键安装

```bash
curl -sSL https://raw.githubusercontent.com/joe12801/autonomous-mining-toolkit/main/install.sh | bash
```

### 完整流程示例

```bash
# Phase 1: 元数据
curl -s https://api.github.com/repos/browser-use/browser-harness | \
    jq '{name, description, stargazers_count, language, pushed_at}'

# Phase 2: 钻探
mkdir -p /tmp/mining/browser-harness
chown joe1280 /tmp/mining/browser-harness
sudo -u joe1280 python3 scripts/driller.py \
    /home/joe1280/repos/browser-harness \
    /tmp/mining/browser-harness/ore

# Phase 3: 图谱
sudo -u joe1280 python3 scripts/graphify update \
    /home/joe1280/repos/browser-harness
cd /home/joe1280/repos/browser-harness/graphify-out
sudo -u joe1280 bash -c "lark drive +upload --file ./graph.html"

# Phase 4: NotebookLM
sudo -u joe1280 notebooklm create "browser-harness 深度开采报告"
# → 保存 UUID
sudo -u joe1280 notebooklm use <uuid>
cp /tmp/mining/browser-harness/ore_part1.txt /tmp/ore.txt
chown joe1280 /tmp/ore.txt
sudo -u joe1280 notebooklm source add /tmp/ore.txt \
    --type file --mime-type "text/plain" --title "browser-harness 源码"
sudo -u joe1280 notebooklm ask "请深度分析架构设计..."

# Phase 5: 飞书文档
sudo -u joe1280 bash -c \
    "cat report.md | lark docs +create --title 'browser-harness 开采报告' --markdown -"

# Phase 6: 发送链接给用户

# Phase 7: Obsidian（可选）
cp report.md /home/joe1280/obsidian-vault/Mining/browser-harness.md
sudo -u joe1280 rclone sync /home/joe1280/obsidian-vault gdrive:ObsidianVault
```

---

## 📊 实战案例

| 项目 | Stars | 飞书报告 |
|------|-------|---------|
| [browser-harness](https://github.com/browser-use/browser-harness) | 8,958 ⭐ | [查看报告](https://www.feishu.cn/docx/Yutmd0wcdoCMAWxd6Okcas60nrh) |
| [obsidian-skills](https://github.com/kepano/obsidian-skills) | 27,992 ⭐ | [查看报告](https://www.feishu.cn/docx/RJjhdDYkZoOlLRxutR2c7zrondc) |

---

## 📁 目录结构

```
autonomous-mining-toolkit/
├── scripts/
│   ├── driller.py              # 源码精炼工具
│   ├── graphify                # 代码图谱构建
│   ├── keep_alive_notebooklm.sh # Session 保活
│   └── sync_google_cookies.py  # Google Cookie 同步（备用）
├── skills/                     # Hermes Agent skill 文件
├── sample_graphify_out/        # 图谱输出示例
├── MINING_SOP.md               # 完整 SOP 文档
├── install.sh                  # 一键安装脚本
└── README.md
```

---

## 🔧 常见问题

| 问题 | 解决方案 |
|------|---------|
| `driller.py` PermissionError | `chown -R joe1280 <输出目录>` |
| `source add` 只读到文件路径 | 使用 `--type file --mime-type "text/plain"` |
| `lark docs create` 失败 | 用 `lark docs +create`（加 `+`） |
| NotebookLM UUID 截断 | 从 `notebooklm create` 输出保存完整 UUID |
| `source add` RPC 失败 | 先运行 `notebooklm use <uuid>` |
| Google Drive 同步失败 | 检查 `rclone listremotes` 是否有 `gdrive:` |

---

*Created and maintained by Hermes Agent · SOP v3.0 · 2026-05-01*
