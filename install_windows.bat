@echo off
echo 🔷 Subtitle Generator Installer for Windows

REM Check for Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python not found. Please install Python 3.8 or newer and rerun this script.
    pause
    exit /b
)

REM Create venv
echo 🔷 Creating virtual environment...
python -m venv venv

REM Activate venv
call venv\Scripts\activate

REM Upgrade pip
echo 🔷 Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 🔷 Installing Python dependencies...
pip install -r requirements.txt
pip install git+https://github.com/openai/whisper.git

REM Download FFmpeg
echo 🔷 Downloading and installing FFmpeg...
powershell -Command ^
    "Invoke-WebRequest -Uri https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip -OutFile ffmpeg.zip"
powershell -Command ^
    "Expand-Archive -Force ffmpeg.zip ."
del ffmpeg.zip
for /D %%d in (ffmpeg-*) do ren "%%d" ffmpeg

echo ✅ FFmpeg downloaded and placed in ffmpeg\bin

echo 🔷 Installation complete!
echo To launch the app, double-click launch_windows.bat
pause
