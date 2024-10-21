@echo off
start cmd /k "title BiliListener v0.1.3 && .\.venv\Scripts\activate && python api.py && pause"
start cmd /k "title FastAPI v0.1.3 && .\.venv\Scripts\activate && python app.py && pause"
