#!/bin/bash
export PYTHONPATH=/opt/notebooklm-shared/notebooklm-py/src
sudo -u joe1280 /root/hermes-agent/venv/bin/python3 -m notebooklm list > /dev/null 2>&1
echo "[$(date)] NotebookLM Heartbeat Sent" >> /root/notebooklm_heartbeat.log
