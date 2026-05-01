#!/bin/bash
# keep_alive_notebooklm.sh — NotebookLM 心跳保活脚本
# 通过 notebooklm list 维持 Google session 活跃

LOG=/home/joe1280/notebooklm_heartbeat.log

sudo -u joe1280 /home/joe1280/notebooklm-py/.venv/bin/notebooklm list > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 心跳成功" >> "$LOG"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 心跳失败" >> "$LOG"
fi

# 只保留最近 200 行日志
tail -200 "$LOG" > "$LOG.tmp" && mv "$LOG.tmp" "$LOG"
