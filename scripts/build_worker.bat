@echo off
title Building Dist......

cd .. && .venv\Scripts\activate && cd app && pyinstaller --onefile worker.py
