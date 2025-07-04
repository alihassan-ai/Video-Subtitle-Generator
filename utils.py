import subprocess
import os
from fontTools.ttLib import TTFont


def extract_audio(video_path, audio_path):
    subprocess.run([
        'ffmpeg', '-y', '-i', video_path, '-q:a', '0', '-map', 'a', audio_path
    ], check=True)


def burn_subtitles(video_path, subtitle_path, output_path, fonts_dir):
    subprocess.run([
        'ffmpeg', '-y', '-i', video_path,
        '-vf', f"subtitles={subtitle_path}:fontsdir={fonts_dir}",
        '-c:v', 'libx264', '-crf', '7', '-preset', 'slow',
        '-c:a', 'copy', output_path
    ], check=True)


def seconds_to_ass_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    cs = int((sec - int(sec)) * 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def get_available_fonts(fonts_folder):
    fonts = []
    if not os.path.exists(fonts_folder):
        return fonts
    for f in os.listdir(fonts_folder):
        if f.lower().endswith(".ttf"):
            fonts.append(f)
    return fonts


def extract_font_name(ttf_filename):
    try:
        font_path = os.path.join("fonts", ttf_filename)
        font = TTFont(font_path)
        for record in font["name"].names:
            if record.nameID == 4:
                return record.string.decode("utf-8", errors="ignore")
    except Exception:
        pass
    return "Arial"

def hex_to_ass_color(hex_color: str) -> str:
    # Convert #RRGGBB → &H00BBGGRR& (ASS format)
    hex_color = hex_color.lstrip("#")
    r, g, b = hex_color[0:2], hex_color[2:4], hex_color[4:6]
    return f"&H00{b}{g}{r}&"

