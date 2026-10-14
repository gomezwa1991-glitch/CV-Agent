@echo off
setlocal
title CV Agent
set PYTHONUTF8=1
"%~dp0.venv\Scripts\python.exe" "C:\Users\gomez\Documents\Codex\2026-10-13\referenced-chatgpt-conversation-this-is-an\outputs\CV-Local-Upgrade\start_agent.py" --legacy %*
pause
