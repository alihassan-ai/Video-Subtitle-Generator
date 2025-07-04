@echo off
echo 🚀 Launching Subtitle Generator

REM Activate venv
call venv\Scripts\activate

REM Add FFmpeg to PATH for this session
set PATH=%CD%\ffmpeg\bin;%PATH%

python app.py
pause
