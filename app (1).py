import gradio as gr
from deep_translator import MyMemoryTranslator

LANGUAGES = [
    "english",
    "french",
    "spanish",
    "german",
    "italian",
    "hindi",
    "telugu"
]

def translate_text(text, source, target):
    if not text.strip():
        return ""

    if source == target:
        return text

    try:
        result = MyMemoryTranslator(
            source=source,
            target=target
        ).translate(text)

        return result

    except Exception as e:
        return f"Translation error: {e}"


with gr.Blocks(title="AI Language Translation Tool") as app:

    gr.Markdown(
        """
        # 🌍 AI Language Translation Tool
        ### Translate text between multiple languages
        """
    )

    text_input = gr.Textbox(
        label="📝 Enter Text",
        placeholder="Type your text here...",
        lines=5
    )

    with gr.Row():

        source_language = gr.Dropdown(
            choices=LANGUAGES,
            value="english",
            label="Source Language"
        )

        target_language = gr.Dropdown(
            choices=LANGUAGES,
            value="french",
            label="Target Language"
        )

    translate_button = gr.Button(
        "🔄 Translate",
        variant="primary"
    )

    output = gr.Textbox(
        label="🌐 Translated Text",
        lines=5
    )

    translate_button.click(
        fn=translate_text,
        inputs=[
            text_input,
            source_language,
            target_language
        ],
        outputs=output
    )

app.launch()
