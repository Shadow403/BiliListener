@echo off
start cmd /k "title BiliListener v0.1.0 && .\.venv\Scripts\activate && python web.py && pause"
start cmd /k "title FastAPI v0.1.0 && .\.venv\Scripts\activate && python app.py && pause"
