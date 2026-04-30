---
name: autonomous-research-mining
description: A 6-stage industrial workflow for deep knowledge extraction from raw sources (YT, Git, PDF) into structured Feishu Wiki entries and Knowledge Graphs.
tags:
  - research
  - notebooklm
  - mining
  - knowledge-graph
  - feishu-wiki
---

# Autonomous Research & Mining Skill 2.0 (Industrial Edition)

## Overview

This skill defines the "Industrial Mining" (工业化采矿) SOP for transforming messy technical sources into structured, permanent knowledge assets within the shared brain (/root/hermes-shared/).

## The "Six-Stage" Industrial Pipeline

### 1. Exploration (勘探)
Use **NotebookLM** for high-volume semantic pre-screening.
- **Goal**: Identify core logic and project scale.
- **Tool**: `sudo -u joe1280 notebooklm source add <URL>`.
- **Note**: Use direct URLs for YouTube/Web; use local refined files for GitHub repos.

### 2. Drilling (钻探) - **Scale-Up Logic**
For codebases that exceed NotebookLM's limits or are "messy" (1GB+):
- **Tool**: `/root/hermes-shared/skills/mining/driller.py`
- **Logic**: 
  1. **De-slagging**: Strip `node_modules`, `vendor`, `.git`, and non-code assets.
  2. **Refining**: Remove empty lines and comments to maximize info density.
  3. **Auto-Sharding**: Split into 5MB chunks (`part1.txt`) to bypass the 10MB cap.
- **Command**: `python3 driller.py <path> <prefix>` then `sudo -u joe1280 notebooklm source add <parts>`.

### 3. Mapping (图谱) - **Locating God Nodes**
Use **Graphify** to detect module coupling.
- **Goal**: Find "God Nodes" (central hubs) to target the Mining stage.
- **Tool**: `graphify update <path>`.
- **Output**: `GRAPH_REPORT.md` (to be integrated into the final report).

### 4. Mining (开采)
Execute deep-dive queries against the refined NotebookLM sources.
- **Standard**: All questions and reports MUST be in **Chinese**.
- **Strategy**: Perform "Cross-file Logic Tracing" based on God Nodes.

### 5. Storage (入库)
Save the refined knowledge into the shared repository.
- **Path**: `/root/hermes-shared/wiki/research/mining-archive/`.
- **Format**: Markdown with `[[Internal Links]]`.

### 6. Synchronization (同步)
Deliver the findings to the User's mobile-accessible knowledge base.
- **Tool**: `@larksuite/cli` (Lark CLI).
- **Process**:
  1. `lark-cli drive +import --file <report.md> --type docx` (for mobile-friendly formatting).
  2. `lark-cli wiki +move --obj-token <token> --target-space-id <SpaceID>` to archive in the **AI Exploration Knowledge Base**.

## Multi-Agent Collaboration

When introducing this workflow to other agents:
1. **Heartbeat**: The `bot_seventh` profile maintains a 60m heartbeat (Job ID `81e908980671`) to keep the Google Session alive.
2. **Auth Consistency**: Always use `sudo -u joe1280` for NotebookLM and Lark operations.
3. **Shared Ingress**: Direct agents to `/root/hermes-shared/wiki/index.md` to discover new mining assets.

## Pitfalls
- **Direct Uploads**: Never upload raw `node_modules`. Always run `driller.py` first.
- **English Bias**: AI defaults to English. Explicitly append "in Chinese" to all mining prompts.
- **Profile Blindness**: Other agents won't see `bot_seventh`'s cronjobs. Instruct them to run `sudo -u joe1280 notebooklm list` to verify health.
