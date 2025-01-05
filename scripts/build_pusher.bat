@echo off
title Building pusher......

cd ..
call .venv\Scripts\activate
cd app
pyinstaller -i ../scripts/ico/listener.ico --onefile pusher.py
pause
