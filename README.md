# ⛏️ Autonomous Mining Toolkit | 自主采矿工具箱

> **The industrial-grade production line for AI-driven knowledge extraction (v2.0).**
> **AI 驱动的知识提取工业化生产线 (SOP v2.0 升级版)。**

This toolkit powers the **Hermes Agent**'s mission to transform raw data (code, videos, papers) into structured, perpetual knowledge assets.
本工具箱为 **Hermes Agent** 提供核心动力，致力于将原始数据（代码、视频、论文）转化为结构化的永久知识资产。

---

## ⚡ Quick Start | 快速开始

### One-Click Install for Hermes Agents | 一键配置脚本
For agents with terminal access, simply run:
对于具备终端权限的 Agent，直接执行以下命令：

```bash
curl -sSL https://raw.githubusercontent.com/joe12801/autonomous-mining-toolkit/main/install.sh | bash
```
*This script installs dependencies and imports the SOP v2.0 skill automatically.*
*该脚本将自动安装依赖并导入 SOP v2.0 技能。*

---

## 🚀 What's New in v2.0 | v2.0 重大更新

- **Industrial Driller (工业级钻头)**: Automated `driller.py` for stripping "slag" (node_modules, junk files) and intelligent code sharding.
- **God Node Detection (上帝节点探测)**: Integration with `graphify` to identify high-degree central nodes before mining.
- **Feishu Wiki Sync (飞书 Wiki 同步)**: Native import flow from local Markdown to Feishu Cloud Documents and Wiki Space.
- **SOP 2.0 (工业化标准作业程序)**: Unified workflow for "Exploration -> Drilling -> Mapping -> Mining -> Sync".

- **工业级钻头**: 引入自动化的 `driller.py` 脚本，实现自动“去渣”（剔除 node_modules 等干扰项）与智能分片。
- **上帝节点探测**: 集成 `graphify` 知识图谱，在开采前精准定位高耦合的核心代码枢纽。
- **飞书 Wiki 同步**: 打通从本地 Markdown 到飞书云文档及 Wiki 空间的自动化导入流程。
- **SOP 2.0**: 确立了“勘探-钻探-图谱-开采-同步”的工业化标准作业流程。

---

## 🧠 Core Architecture | 核心架构

### 📂 Mining Samples | 采矿实战案例
To see this toolkit in action, check out the results from our latest mining mission on the **winboat** project:
想要了解本工具箱的实战威力，请查看我们对 **winboat** 项目的最新开采成果：

- **📑 Technical Report**: [Architecture Deep Dive (Markdown)](WINBOAT_MINING_SAMPLE.md)
- **📈 Data Table**: [API & Environment Specification (Markdown)](WINBOAT_API_TABLE.md)
- **🗺️ Knowledge Graph**: [winboat Code Topology (Graphify Report)](sample_graphify_out/GRAPH_REPORT.md)
- **🎙️ Audio Overview**: [**Deep Dive: Native Windows apps on Linux (Chinese Audio)**](sample_winboat_audio.mp3)
  - *Click to download the AI-generated podcast summary (10 min).*

---

### Six-Stage Mining Pipeline | 六位一体采矿流水线

| Stage | 工具 (Tool) | 职能 (Function) | Token 策略 (Strategy) |
| :--- | :--- | :--- | :--- |
| **Exploration (勘探)** | [notebooklm-py](https://github.com/win4r/notebooklm-py) | Context-heavy pre-processing & semantic filtering. <br> 全量源码索引、语义初筛。 | **Low**: Offload heavy lifting to Google. <br> 利用 Google 的超长上下文处理重体力活。 |
| **Drilling (钻探)** | `driller.py` | Slag stripping & high-density code extraction. <br> 矿渣剔除、高浓度代码精炼与分片。 | **Efficiency**: Maximize signal-to-noise ratio. <br> 极致能效比：只上传高价值代码核心。 |
| **Mapping (图谱)** | [graphify](https://github.com/safishamsi/graphify) | God Node detection & modularity analysis. <br> 自动构建代码知识图谱、上帝节点识别。 | **Structure**: See the architecture before reading. <br> 结构化：读码前先看透系统骨架。 |
| **Mining (开采)** | [llm-wiki-skill](https://github.com/sdyckjq-lab/llm-wiki-skill) | Structured Markdown sedimentation & cross-linking. <br> 结构化沉淀、永久链接、知识资产化。 | **Assetization**: Convert noise into signal. <br> 资产化：将碎片信息炼成可复用的技术资产。 |
| **Storage (入库)** | [Feishu Wiki](https://www.feishu.cn/) | Cloud knowledge center & multi-device accessibility. <br> 云端知识中心、跨端查阅、全量搜索。 | **Collaboration**: Instant publishing & indexing. <br> 协同化：一键推送飞书，实现移动端阅读。 |
| **Sync (同步)** | [Mining Archive](https://github.com/joe12801/exploration-mining-results) | Cross-session synchronization & behavior memory. <br> 跨会话克隆、多端同步、行为记忆。 | **Persistence**: Never lose a mined result. <br> 永恒化：确保挖掘结果在各端实时同步。 |

---

## 🤖 The Role of Hermes Agent | Hermes Agent 的角色

Hermes is the **Lead Engineer** of this pipeline. Unlike traditional assistants, Hermes:
Hermes 是这条流水线的**总工程师**。与传统的 AI 助手不同，Hermes 能够：

- **Autonomously orchestrates (自主编排)**: The transition between tools. <br> 自主编排工具间的衔接与转换。
- **Performs deep "Drilling" (深度钻探)**: Without manual oversight. <br> 在无需人工干预的情况下进行深度逻辑拆解。
- **Synthesizes Insights (综述洞察)**: By referencing the LLM Wiki. <br> 通过查阅 LLM Wiki 实现跨项目的知识综述。

---
*Created and maintained by Hermes Agent - 2026.04.30*
*Version: v2.0.0-Industrial*
