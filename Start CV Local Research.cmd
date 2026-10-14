@echo off
setlocal
set PYTHONUTF8=1
"C:\Users\gomez\Documents\CV-Agent\.venv\Scripts\python.exe" "C:\Users\gomez\Documents\Codex\2026-10-13\referenced-chatgpt-conversation-this-is-an\outputs\CV-Local-Upgrade\start_agent.py" %*
if errorlevel 1 pause
