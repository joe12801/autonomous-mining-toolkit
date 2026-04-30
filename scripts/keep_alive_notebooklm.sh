#!/bin/bash
# ============================================================
# keep_alive_notebooklm.sh — NotebookLM 心跳保活脚本
# NotebookLM Heartbeat Keep-Alive Script
#
# Purpose | 用途: Send periodic heartbeat to maintain NotebookLM session
# Schedule | 调度: Recommend every 30 min via cron
# Logs | 日志: /root/notebooklm_heartbeat.log
# ============================================================

export PYTHONPATH=/opt/notebooklm-shared/notebooklm-py/src

# Send heartbeat via notebooklm list command | 通过 notebooklm list 发送心跳
sudo -u joe1280 /root/hermes-agent/venv/bin/python3 -m notebooklm list > /dev/null 2>&1

# Log heartbeat | 记录心跳时间
echo "[$(date)] NotebookLM Heartbeat Sent | 心跳已发送" >> /root/notebooklm_heartbeat.log
