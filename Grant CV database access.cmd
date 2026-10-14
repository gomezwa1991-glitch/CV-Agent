@echo off
:: Run this once. It asks for administrator permission, then gives your Windows login
:: access to the Cabinet Vision 2025 catalog database so the agent can manage UCS.
net session >nul 2>&1
if %errorlevel% neq 0 (
  powershell -NoProfile -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
  exit /b
)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\grant-db-access.ps1"
