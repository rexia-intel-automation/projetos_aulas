@echo off
cd /d "%~dp0"
echo Iniciando protótipo CMDPII...
python serve.py
if errorlevel 1 pause
