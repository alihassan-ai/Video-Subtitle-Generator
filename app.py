import os
import gradio as gr
from process import process_video
from utils import get_available_fonts

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def subtitle_folder(folder_path, font_file, fontsize, highlight_size, text_color, highlight_color, words_per_line):
    results = []

    config = {
        "font_file": font_file,
        "fontsize": fontsize,
        "highlight_size": highlight_size,
        "text_color": text_color,
        "highlight_color": highlight_color,
        "words_to_show": words_per_line
    }

    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            full_path = os.path.join(folder_path, filename)
            try:
                result = process_video(full_path, OUTPUT_DIR, config)
                results.append(result)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return results


def load_fonts():
    fonts = get_available_fonts("fonts")
    return gr.update(choices=fonts, value=fonts[0] if fonts else None)


with gr.Blocks() as demo:
    gr.Markdown("# 🎬 Subtitle Generator with Custom Styling")
    gr.Markdown("Control subtitle font, size, color, highlight, and how many words to show per line.")

    with gr.Row():
        with gr.Column():
            folder_input = gr.Textbox(label="📁 Folder path with .mp4 videos", value="videos/")
            font_dropdown = gr.Dropdown(label="🖋 Font (from fonts/ folder)", choices=[], interactive=True)
            base_size = gr.Slider(30, 100, value=48, label="🧱 Base font size")
            highlight_size = gr.Slider(50, 150, value=70, label="🌟 Highlighted word font size")
            text_color = gr.ColorPicker(value="#FFFFFF", label="🎨 Text Color")
            highlight_color = gr.ColorPicker(value="#00FFFF", label="🎯 Highlight Color")
            words_per_line = gr.Slider(1, 10, step=1, value=3, label="📝 Words per subtitle group")
            submit_btn = gr.Button("🚀 Submit")

        with gr.Column():
            output_gallery = gr.Gallery(label="🎞 Final Subtitled Videos", columns=[2])

    submit_btn.click(
        fn=subtitle_folder,
        inputs=[
            folder_input, font_dropdown, base_size,
            highlight_size, text_color, highlight_color, words_per_line
        ],
        outputs=output_gallery
    )

    # Dynamically load fonts on interface load
    demo.load(fn=load_fonts, inputs=[], outputs=font_dropdown)

demo.launch(share=True)
