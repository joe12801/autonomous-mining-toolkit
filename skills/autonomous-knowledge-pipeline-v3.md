---
name: autonomous-knowledge-pipeline-v3
description: "6-stage Exploration-Mining pipeline: NotebookLM bulk exploration → surgical code drilling → LLM Wiki crystallization → Graphify mapping → Feishu Wiki storage → GitHub archiving. Token-efficient knowledge asset creation from codebases."
---

# Exploration-Mining Knowledge Pipeline (勘探-采矿)

Token-efficient 6-stage pipeline for turning codebases into structured, permanent knowledge assets. Based on the joe12801 exploration-mining methodology.

## Philosophy: Tiered Token Economy

| Stage | Tool | Role | Token Strategy |
|:---|:---|:---|:---|
| **1. 勘探** | NotebookLM | Full-source indexing, audio overview | **Free**: Google's ultra-long context |
| **2. 钻探** | Hermes Agent | Algorithm cracking, code deep-dive | **Surgical**: Only key code paths |
| **3. 开采** | llm-wiki | Structured crystallization, linking | **Asset**: One-time write, forever query |
| **4. 图谱** | Graphify | Knowledge graph, community detection | **Visual**: God nodes, surprises |
| **5. 入库** | Feishu Wiki | Cloud center, cross-platform access | **Access**: Mobile, search, share |
| **6. 同步** | GitHub Archive | Cross-session memory, AI "hard drive" | **Persistence**: Survives resets |

**Rule**: NotebookLM does the bulk for free. Hermes only drills what matters.

## Stage 1: Exploration (NotebookLM)

Load `notebooklm` skill. Create notebook, add repo source, generate audio overview:

```bash
notebooklm create "Exploration: <Project>"
notebooklm source add "https://github.com/owner/repo"
notebooklm source wait <source_id>
notebooklm generate audio "Focus on architecture, key algorithms, design patterns" --json
notebooklm ask "What are the 3-5 most important modules?"
```

**Decision gate**: After overview, pick 2-4 "drill targets". Do NOT drill everything.

## Stage 2: Drilling (Code Deep-Dive)

Clone repo, build structural map, read only critical code:

```bash
gh repo clone owner/repo /tmp/drill_target
graphify /tmp/drill_target        # AST-first structural map
```

Answer for each drill target:
- Core algorithm/mechanism?
- Non-obvious design decisions?
- Optimization tricks?
- Limitations?

**Rule**: Read the MINIMUM code. NotebookLM already read everything.

## Stage 3: Mining (LLM Wiki Crystallization)

Load `llm-wiki` skill. Use this template for every discovery:

```markdown
# [Project]: [Key Finding]

> [!TIP] ✅ Core Insight
> One-line summary of the discovery.

## 1. [Deep-Dive Section]
Technical details, code paths.

## 2. [Second Section]
Comparative insights, architecture tables.

| Dimension | Implementation |
|-----------|---------------|
| **Language** | ... |
| **Key Tech** | ... |

## N. Lessons & Applications
---
*📍 Source: [URL]*
*📅 Mining Date: YYYY-MM-DD*
```

Save to `~/wiki/entities/<project>_<topic>.md`. Link from `index.md`.

## Stage 4: Mapping (Graphify)

```bash
cd /tmp/drill_target && graphify .
```

Review `graphify-out/graph.html` (interactive) and `GRAPH_REPORT.md` (god nodes, surprising connections).

## Stage 5: Storage (Feishu Wiki)

Load `feishu-lark-cli` skill:

```bash
lark drive upload ~/wiki/entities/<report>.md
```

## Stage 6: Sync (GitHub Archive)

```bash
cd exploration-mining-results
cp ~/wiki/entities/<report>.md mining_reports/
git add mining_reports/ && git commit -m "mining: <project> — <finding>" && git push
```

## Quick Reference

| Starting Point | Begin at Stage |
|---------------|----------------|
| New repo, no knowledge | 1 (full pipeline) |
| Know the code, want depth | 2 (drilling) |
| Have analysis, need to crystallize | 3 (mining) |
| Need navigable code map | 4 (mapping) |
| Just publish existing findings | 5 (storage) |

## Pitfalls

- **NotebookLM rate limits**: Audio generation may fail. Retry after 5-10 min.
- **Token budget**: Never full semantic extraction on 1000+ file repos — AST for bulk, semantic for key modules.
- **Report drift**: Archived reports drift from live code. Re-run on major upstream changes.
- **Feishu 15MB cap**: Split large reports with `split -b 15M`.
- **Sub-skills**: This is an orchestrator. Load `notebooklm`, `graphify`, `llm-wiki`, `feishu-lark-cli` as needed — don't duplicate their content.