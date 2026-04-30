---
name: autonomous-knowledge-pipeline-v3
description: "6-stage Exploration-Mining pipeline | 六阶段勘探-采矿流水线: NotebookLM bulk exploration → surgical code drilling → LLM Wiki crystallization → Graphify mapping → Feishu Wiki storage → GitHub archiving. Token-efficient knowledge asset creation from codebases."
---

# Exploration-Mining Knowledge Pipeline | 勘探-采矿知识流水线

> Token-efficient 6-stage pipeline for turning codebases into structured, permanent knowledge assets.
> 低 Token 成本的六阶段流水线，将代码库转化为结构化的永久知识资产。

Based on the joe12801 exploration-mining methodology | 基于 joe12801 勘探-采矿方法论。

---

## Philosophy: Tiered Token Economy | 理念：分层 Token 经济

| Stage | 阶段 | Tool | 工具 | Role | 职能 | Token Strategy | Token 策略 |
|:---|:---|:---|:---|:---|:---|:---|
| **1. Exploration** | 勘探 | NotebookLM | Full-source indexing, audio overview | 全量索引、音频综述 | **Free** | 免费：Google 超长上下文 |
| **2. Drilling** | 钻探 | Hermes Agent | Algorithm cracking, code deep-dive | 算法破解、代码深挖 | **Surgical** | 外科手术式：仅关键路径 |
| **3. Mining** | 开采 | llm-wiki | Structured crystallization, linking | 结构化沉淀、永久链接 | **Asset** | 资产化：一次写入，永久查询 |
| **4. Mapping** | 图谱 | Graphify | Knowledge graph, community detection | 知识图谱、社区检测 | **Visual** | 可视化：God Nodes、意外发现 |
| **5. Storage** | 入库 | Feishu Wiki | Cloud center, cross-platform access | 云端中心、跨端查阅 | **Access** | 访问：移动端、搜索、分享 |
| **6. Sync** | 同步 | GitHub Archive | Cross-session memory, AI "hard drive" | 跨会话记忆、AI "外部硬盘" | **Persistence** | 持久化：跨重置存活 |

**Rule | 原则**: NotebookLM does the bulk for free. Hermes only drills what matters.
NotebookLM 免费干重活，Hermes 只钻探关键点。

---

## Stage 1: Exploration (NotebookLM) | 第一阶：勘探

Load `notebooklm` skill. Create notebook, add repo source, generate audio overview:
加载 `notebooklm` 技能，创建笔记本，添加源码，生成音频综述：

```bash
notebooklm create "Exploration: <Project>"          # 创建勘探笔记本
notebooklm source add "https://github.com/owner/repo" # 添加源码
notebooklm source wait <source_id>                  # 等待索引完成
notebooklm generate audio "Focus on architecture, key algorithms, design patterns" --json
notebooklm ask "What are the 3-5 most important modules?"  # 询问核心模块
```

**Decision gate | 决策关卡**: After overview, pick 2-4 "drill targets". Do NOT drill everything.
听完综述后，选取 2-4 个"钻探目标"。不要钻探所有代码。

---

## Stage 2: Drilling (Code Deep-Dive) | 第二阶：钻探

Clone repo, build structural map, read only critical code:
克隆仓库，构建结构图谱，仅读取关键代码：

```bash
gh repo clone owner/repo /tmp/drill_target   # 克隆目标仓库
graphify /tmp/drill_target                   # AST优先的结构图谱
```

Answer for each drill target | 对每个钻探目标回答：
- Core algorithm/mechanism? | 核心算法/机制？
- Non-obvious design decisions? | 非显而易见的设计决策？
- Optimization tricks? | 优化技巧？
- Limitations? | 局限性？

**Rule | 原则**: Read the MINIMUM code. NotebookLM already read everything.
只读最少量的代码——NotebookLM 已经读了全部。

---

## Stage 3: Mining (LLM Wiki Crystallization) | 第三阶：开采

Load `llm-wiki` skill. Use this template for every discovery:
加载 `llm-wiki` 技能。每次发现使用以下模板：

```markdown
# [Project]: [Key Finding] | 项目：核心发现

> [!TIP] ✅ Core Insight | 核心洞察
> One-line summary of the discovery. | 发现的单行总结。

## 1. [Deep-Dive Section] | 深度分析
Technical details, code paths. | 技术细节、代码路径。

## 2. [Second Section] | 第二部分
Comparative insights, architecture tables. | 对比洞察、架构表格。

| Dimension | 维度 | Implementation | 实现 |
|-----------|------|---------------|------|
| **Language** | 语言 | ... | ... |
| **Key Tech** | 核心技术 | ... | ... |

## N. Lessons & Applications | 经验与应用
---
*📍 Source | 来源: [URL]*
*📅 Mining Date | 采矿日期: YYYY-MM-DD*
```

Save to `~/wiki/entities/<project>_<topic>.md`. Link from `index.md`.
保存到 `~/wiki/entities/<project>_<topic>.md`，从 `index.md` 添加链接。

---

## Stage 4: Mapping (Graphify) | 第四阶：图谱

```bash
cd /tmp/drill_target && graphify .   # 在目标目录生成图谱
```

Review `graphify-out/graph.html` (interactive | 交互式) and `GRAPH_REPORT.md` (god nodes | 核心节点, surprising connections | 意外连接).

---

## Stage 5: Storage (Feishu Wiki) | 第五阶：入库

Load `feishu-lark-cli` skill | 加载飞书技能：

```bash
lark drive upload ~/wiki/entities/<report>.md  # 上传到飞书云盘
```

---

## Stage 6: Sync (GitHub Archive) | 第六阶：同步

```bash
cd exploration-mining-results
cp ~/wiki/entities/<report>.md mining_reports/   # 复制报告
git add mining_reports/
git commit -m "mining: <project> — <finding>"    # 提交
git push                                          # 推送
```

---

## Quick Reference | 快速参考

| Starting Point | 起点 | Begin at Stage | 从哪阶开始 |
|:---|:---|:---|:---|
| New repo, no knowledge | 新仓库，零知识 | 1 (full pipeline | 全流程) |
| Know the code, want depth | 懂代码，要深度 | 2 (drilling | 钻探) |
| Have analysis, need to crystallize | 有分析，需沉淀 | 3 (mining | 开采) |
| Need navigable code map | 需要代码导航图 | 4 (mapping | 图谱) |
| Just publish existing findings | 发布已有成果 | 5 (storage | 入库) |

---

## Pitfalls | 常见陷阱

- **NotebookLM rate limits | 速率限制**: Audio generation may fail. Retry after 5-10 min.
  音频生成可能失败，等 5-10 分钟后重试。
- **Token budget | Token 预算**: Never full semantic extraction on 1000+ file repos — AST for bulk, semantic for key modules.
  1000+ 文件仓库绝不做全量语义提取——AST 做全量，语义只管核心模块。
- **Report drift | 报告漂移**: Archived reports drift from live code. Re-run on major upstream changes.
  归档报告会与实时代码漂移，上游大变更时重新运行。
- **Feishu 15MB cap | 飞书 15MB 限制**: Split large reports with `split -b 15M`.
  大报告用 `split -b 15M` 分片。
- **Sub-skills | 子技能**: This is an orchestrator. Load `notebooklm`, `graphify`, `llm-wiki`, `feishu-lark-cli` as needed — don't duplicate their content.
  这是编排器，按需加载子技能，不要复制其内容。
