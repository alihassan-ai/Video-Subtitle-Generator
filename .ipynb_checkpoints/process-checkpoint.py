import os
import whisper
from utils import (
    extract_audio,
    burn_subtitles,
    seconds_to_ass_time,
    extract_font_name,
    hex_to_ass_color
)

model = whisper.load_model("medium")

def generate_ass(transcript, ass_path, config):
    from utils import hex_to_ass_color, extract_font_name, seconds_to_ass_time

    font_name = extract_font_name(config["font_file"])
    fontsize = config["fontsize"]
    highlight_size = config["highlight_size"]
    text_color = hex_to_ass_color(config["text_color"])
    highlight_color = hex_to_ass_color(config["highlight_color"])
    words_per_group = config["words_to_show"]

    ass = f"""[Script Info]
Title: Dynamic Subtitles
ScriptType: v4.00+
PlayResX:1280
PlayResY:720

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,{font_name},{fontsize},{text_color},&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    for seg in transcript["segments"]:
        words = seg.get("words", [])
        if not words:
            continue

        # slide window over words
        for i in range(0, len(words)):
            group_start = max(0, i - (words_per_group // 2))
            group_end = min(len(words), group_start + words_per_group)
            group = words[group_start:group_end]

            start = seconds_to_ass_time(words[i]["start"])
            end = seconds_to_ass_time(words[i]["end"])

            line = []
            for j, word in enumerate(group):
                word_text = word["word"].strip()
                if group_start + j == i:
                    # currently spoken word
                    styled = f"{{\\fs{highlight_size}\\c{highlight_color}}}{word_text}{{\\r}}"
                else:
                    styled = word_text
                line.append(styled)

            text = " ".join(line)
            ass += f"Dialogue: 0,{start},{end},Default,,0,0,0,,{text}\n"

    with open(ass_path, "w") as f:
        f.write(ass)



def process_video(video_path, output_folder, config):
    os.makedirs(output_folder, exist_ok=True)

    base = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_folder, f"{base}.mp3")
    ass_path = os.path.join(output_folder, f"{base}.ass")
    final_path = os.path.join(output_folder, f"{base}_subtitled.mp4")

    extract_audio(video_path, audio_path)

    try:
        result = model.transcribe(audio_path, word_timestamps=True, verbose=False)
    except Exception as e:
        raise RuntimeError(f"Whisper transcription failed: {e}")

    generate_ass(result, ass_path, config)

    try:
        burn_subtitles(video_path, ass_path, final_path, fonts_dir="fonts")
    except Exception as e:
        raise RuntimeError(f"FFmpeg failed to burn subtitles: {e}")

    return final_path
