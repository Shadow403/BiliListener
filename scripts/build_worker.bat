@echo off
title Building worker......

cd ..
call .venv\Scripts\activate
cd app
pyinstaller -i ../scripts/ico/websocket.ico --onefile worker.py
pause
