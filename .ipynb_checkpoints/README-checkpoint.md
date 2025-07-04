# 🎬 Subtitle Generator karaoke style (word by word highlighting)

This project lets you generate and burn high-quality, word-by-word **highlighted subtitles** on your videos using OpenAI Whisper, FFmpeg, and a web-based UI.  
✅ Works on nearly 100 languages.  
✅ Input: Normal Video -> output: Subtitled video
✅ No technical skills required — just copy-paste the commands below.

---

## 🚀 Features & Capabilities

✅ Automatically transcribes audio to text using Whisper (supports ~100 languages)  
✅ Highlights each word as it is spoken (karaoke-style)  
✅ Supports custom fonts, colors, sizes, and word grouping  
✅ Burns the subtitles directly onto the video  
✅ Web-based UI (no need to use the terminal after setup)  
✅ Works on any video with spoken audio (.mp4 recommended)  
✅ GPU acceleration (if available)  

---

## 🖥️ Prerequisites

✅ Linux, macOS, or Windows (with Git Bash or Command Prompt)  
✅ Python ≥ 3.8 installed  
✅ Around 8–12 GB RAM recommended
✅ FFmpeg installed (see below for installation instructions)
✅ OpenAI Whisper installed (see below for installation instructions)
✅ Minimum of 3 GB VRAM available
✅ If running locally: make sure you have permissions to install packages

---

## 📥 Installation & Setup

— just follow these steps:

### 1️⃣ Clone this repo:
```bash
git clone https://github.com/alihassan-ai/Video-Subtitle-Generator.git
cd video-subtitler
```

---

#### Installation On Linux / macOS:
Open a terminal and navigate to video-subtitler directory
Run the following commands to install the app
```bash
chmod +x ./install.sh
./install.sh
```

---

## ▶️ How to Launch

After installing, simply run:
```bash
chmod +x ./run.sh
./run.sh
```

The terminal will show a link — open it in your browser to use the app.

---

#### 🪟 On Windows:
1) Navigate to Video-subtitle generator Folder 
2) Click on Install windows.bat file
3) Command prompt will open infront of you and everyhting will be installed automatically.
4) After installation is complete, click on run.bat file to launch the app.




## 📝 How to Use

✅ Put your `.mp4` videos in the `videos/` folder  
✅ Put your `.ttf` fonts in the `fonts/` folder (optional, recommended for non-Latin languages)  
✅ Launch the app (`launch.sh`)  
✅ In the web UI:
- Enter the folder path
- Pick your font, colors, sizes
- Hit **Submit**
✅ Find the final subtitled videos in the `output/` folder

---

## 🌏 Supported Languages

The app can transcribe and subtitle in ~100 languages, including:  
English, Spanish, French, German, Chinese, Arabic, Hindi, Japanese, Korean, Russian, Portuguese, Turkish, Dutch, Greek, Polish, Vietnamese, and many more.

It auto-detects the spoken language — no need to set anything!

---

## 📂 Folder Structure

```
video-subtitler/
├── app.py              # Web UI
├── process.py          # Subtitle generation logic
├── utils.py            # Helper functions
├── install_linux.sh    # Installer script for Linux/macOS
├── install_windows.bat # Installer script for Windows
├── launch.sh           # Launch script
├── README.md
├── requirements.txt
├── fonts/              # Place .ttf font files here
├── videos/             # Place .mp4 video files here
└── output/             # Final videos appear here
```

---

## 🆘 Troubleshooting

❓ Fonts not showing?  
Make sure you put `.ttf` files into the `fonts/` folder.

---

## 📝 LICENSE

MIT License

---

Made with ❤️ and low-level madness by AI Dude at woweffect.ai

---

### 🚀 TL;DR

If you’d like, this can also be packaged into:  
✅ Docker container  
✅ HuggingFace Spaces  
✅ Prebuilt `.exe` or `.app` installer  

Just open an issue or contribute 🚀✨