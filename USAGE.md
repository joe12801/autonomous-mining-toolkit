# 🛠️ Usage Guide: How to Operate the Mining Pipeline

This guide is designed for **AI Agents** and **Technical Operators** to ensure consistent knowledge production.

## 1. Environment Prerequisites
Before running the pipeline, ensure the following tools are globally accessible:
- **NotebookLM CLI**: `sudo -u joe1280 notebooklm` (requires active session).
- **Graphify Engine**: Path at `/root/graphify/src`.
- **Lark CLI**: `lark-cli` (v1.0.14+) with valid `auth login`.
- **Shared Center**: All data must be symlinked to `/root/hermes-shared/`.

## 2. Standard Operation Procedure (SOP)

### Phase 1: Exploration (Semantic Ingestion)
```bash
# Add source to NotebookLM
sudo -u joe1280 notebooklm source add <URL_OR_FILE>

# Ask for initial summary
sudo -u joe1280 notebooklm ask "Summarize the core architecture and list 5 key entities."
```

### Phase 2: Mapping (Graph Construction)
```bash
# Generate knowledge graph for a local codebase
cd /path/to/project
export PYTHONPATH=$PYTHONPATH:/root/graphify/src
python3 /root/graphify/graphify.py create . --output ./graphify-out
```

### Phase 3: Drilling & Mining (Hermes Protocol)
1. Load the `autonomous-research-mining` skill.
2. Analyze the `graph.json` and `GRAPH_REPORT.md` from Phase 2.
3. Synthesize the findings into a standard Markdown report.

### Phase 4: Storage (Feishu Wiki Sync)
```bash
# Create a new Wiki node
sudo -u joe1280 lark-cli wiki +node-create --space-id <SPACE_ID> --title "[Mined] Project Name" --obj-type "docx"

# Sync content (Preferred: drive +import)
sudo -u joe1280 lark-cli drive +import --file "./report.md" --type "docx" --folder-token <FOLDER_TOKEN>
```

## 3. Directory Layout
- `/root/hermes-shared/wiki/`: Permanent knowledge base.
- `/root/hermes-shared/wiki/research/mining-archive/`: Raw mining reports.
- `/root/autonomous-mining-toolkit/scripts/`: Automation binaries.

## 4. Agent Handover Protocol
When a new agent takes over, it MUST:
1. Run `ls -R /root/hermes-shared/wiki/` to index existing knowledge.
2. Check `autonomous-mining-toolkit/README.md` for the latest architecture version.
3. Verify the NotebookLM heartbeat status via `crontab -l`.

---
*Maintained by Hermes Agent - 2026.04.29*
