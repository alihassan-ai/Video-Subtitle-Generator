#!/bin/bash

echo "🔷 Subtitle Generator Installer for Linux/Mac..."

# Check Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found. Please install Python 3.8 or newer."
    exit
fi

# Install FFmpeg
echo "🔷 Installing FFmpeg..."
sudo apt update && sudo apt install -y ffmpeg git python3-venv unzip

# Create venv
echo "🔷 Creating virtual environment..."
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Upgrade pip
echo "🔷 Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "🔷 Installing Python dependencies..."
pip install -r requirements.txt
pip install git+https://github.com/openai/whisper.git

echo "✅ Installation complete. To launch, run: ./launch_linux.sh"