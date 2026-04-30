# 🛠️ Usage Guide | 使用指南

> How to Operate the Mining Pipeline | 采矿流水线操作指南

This guide is designed for **AI Agents** and **Technical Operators** to ensure consistent knowledge production.
本指南面向 **AI Agent** 和 **技术运维人员**，确保知识产出的标准一致性。

---

## 1. Environment Prerequisites | 环境前提

Before running the pipeline, ensure the following tools are globally accessible:
运行流水线前，请确保以下工具全局可用：

| Tool | 工具 | Requirement | 要求 |
|:---|:---|:---|
| **NotebookLM CLI** | 命令行 | `sudo -u joe1280 notebooklm` (requires active session / 需要活跃会话) |
| **Graphify Engine** | 图谱引擎 | Path at `/root/graphify/src` |
| **Lark CLI** | 飞书命令行 | `lark-cli` (v1.0.14+) with valid `auth login` / 已登录 |
| **Shared Center** | 共享中心 | All data must be symlinked to `/root/hermes-shared/` / 全部数据须链接到 `/root/hermes-shared/` |

---

## 2. Standard Operation Procedure (SOP) | 标准操作流程

### Phase 1: Exploration (Semantic Ingestion) | 第一阶：勘探（语义摄入）

```bash
# Add source to NotebookLM | 添加源到 NotebookLM
sudo -u joe1280 notebooklm source add <URL_OR_FILE>

# Ask for initial summary | 请求初始摘要
sudo -u joe1280 notebooklm ask "Summarize the core architecture and list 5 key entities."
# 中文: "总结核心架构并列出具 5 个关键实体。"
```

### Phase 2: Mapping (Graph Construction) | 第二阶：图谱（知识图谱构建）

```bash
# Generate knowledge graph for a local codebase | 为本地代码库生成知识图谱
cd /path/to/project
export PYTHONPATH=$PYTHONPATH:/root/graphify/src
python3 /root/graphify/graphify.py create . --output ./graphify-out
```

### Phase 3: Drilling & Mining (Hermes Protocol) | 第三阶：钻探与开采（Hermes 协议）

1. Load the `autonomous-research-mining` skill. | 加载 `autonomous-research-mining` 技能。
2. Analyze the `graph.json` and `GRAPH_REPORT.md` from Phase 2. | 分析第二阶段产出的 `graph.json` 和 `GRAPH_REPORT.md`。
3. Synthesize the findings into a standard Markdown report. | 将发现综合为标准 Markdown 报告。

### Phase 4: Storage (Feishu Wiki Sync) | 第四阶：入库（飞书知识库同步）

```bash
# Create a new Wiki node | 创建新的 Wiki 节点
sudo -u joe1280 lark-cli wiki +node-create --space-id <SPACE_ID> \
  --title "[Mined] Project Name" --obj-type "docx"

# Sync content (Preferred: drive +import) | 同步内容（推荐：drive +import）
sudo -u joe1280 lark-cli drive +import --file "./report.md" \
  --type "docx" --folder-token <FOLDER_TOKEN>
```

---

## 3. Directory Layout | 目录布局

| Path | 路径 | Purpose | 用途 |
|:---|:---|:---|
| `/root/hermes-shared/wiki/` | Permanent knowledge base | 永久知识库 |
| `/root/hermes-shared/wiki/research/mining-archive/` | Raw mining reports | 原始采矿报告 |
| `/root/autonomous-mining-toolkit/scripts/` | Automation binaries | 自动化脚本 |

---

## 4. Agent Handover Protocol | Agent 交接协议

When a new agent takes over, it **MUST** | 新 Agent 接管时**必须**执行：

| # | Step | 步骤 |
|:---|:---|:---|
| 1 | Run `ls -R /root/hermes-shared/wiki/` to index existing knowledge | 运行 `ls -R /root/hermes-shared/wiki/` 索引已有知识 |
| 2 | Check `autonomous-mining-toolkit/README.md` for the latest architecture version | 检查 `autonomous-mining-toolkit/README.md` 获取最新架构版本 |
| 3 | Verify the NotebookLM heartbeat status via `crontab -l` | 通过 `crontab -l` 验证 NotebookLM 心跳状态 |

---

*Maintained by Hermes Agent — 2026.04.30*
*由 Hermes Agent 维护 — 2026.04.30*
