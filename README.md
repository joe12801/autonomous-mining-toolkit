# ⛏️ Autonomous Mining Toolkit | 自主采矿工具箱

> **The industrial-grade production line for AI-driven knowledge extraction.**
> **AI 驱动的知识提取工业化生产线。**

This toolkit powers the **Hermes Agent**'s mission to transform raw data (code, videos, papers) into structured, perpetual knowledge assets.
本工具箱为 **Hermes Agent** 提供核心动力，致力于将原始数据（代码、视频、论文）转化为结构化的永久知识资产。

---

## 🧠 Core Architecture | 核心架构
### Six-Stage Mining Pipeline | 六位一体采矿流水线

| Stage | 工具 (Tool) | 职能 (Function) | Token 策略 (Strategy) |
| :--- | :--- | :--- | :--- |
| **Exploration (勘探)** | [notebooklm-py](https://github.com/win4r/notebooklm-py) | Context-heavy pre-processing & semantic filtering. <br> 全量源码索引、语义初筛、音频综述。 | **Low**: Offload heavy lifting to Google. <br> 利用 Google 的超长上下文处理重体力活。 |
| **Drilling (钻探)** | **Hermes Agent** | Deep code analysis, logic tracing & root cause analysis. <br> 核心算法破解、代码级深挖、逻辑溯源。 | **Surgical**: High-precision focus on critical code. <br> 外科手术式：只读关键代码，把钱花在刀刃上。 |
| **Mining (开采)** | [llm-wiki-skill](https://github.com/sdyckjq-lab/llm-wiki-skill) | Structured Markdown sedimentation & cross-linking. <br> 结构化沉淀、永久链接、知识资产化。 | **Assetization**: Convert noise into signal. <br> 资产化：将碎片信息炼成可复用的技术文档。 |
| **Mapping (图谱)** | [graphify](https://github.com/safishamsi/graphify) | Knowledge graph construction & community detection. <br> 自动构建代码知识图谱、社区检测。 | **Visualization**: See the "God Nodes". <br> 可视化：直观展示模块耦合与核心枢纽。 |
| **Storage (入库)** | [Feishu Wiki](https://www.feishu.cn/) | Cloud knowledge center & multi-device accessibility. <br> 云端知识中心、跨端查阅、全量搜索。 | **Collaboration**: Instant publishing & indexing. <br> 协同化：一键推送飞书，实现移动端即时采矿。 |
| **Sync (同步)** | [Mining Archive](https://github.com/joe12801/exploration-mining-results) | Cross-session synchronization & behavior memory. <br> 跨会话克隆、多端同步、行为记忆。 | **Persistence**: Never lose a mined result. <br> 永恒化：确保挖掘结果在各端实时同步。 |

---

## 🤖 The Role of Hermes Agent | Hermes Agent 的角色

Hermes is the **Lead Engineer** of this pipeline. Unlike traditional assistants, Hermes:
Hermes 是这条流水线的**总工程师**。与传统的 AI 助手不同，Hermes 能够：

- **Autonomously orchestrates (自主编排)**: The transition between tools. <br> 自主编排工具间的衔接与转换。
- **Performs deep "Drilling" (深度钻探)**: Without manual oversight. <br> 在无需人工干预的情况下进行深度逻辑拆解。
- **Synthesizes Insights (综述洞察)**: By referencing the LLM Wiki. <br> 通过查阅 LLM Wiki 实现跨项目的知识综述。

---
*Created and maintained by Hermes Agent - 2026.04.29*
