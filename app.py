import gradio as gr
import transformers

def translate_with_prefix(English):
    prefix = "Translate English to Latin: "
    translator = transformers.pipeline("translation", model="AlbertY123/translator-en-la") 
    return translator(prefix + English)

iface = gr.Interface(fn=translate_with_prefix, 
                     inputs="text", 
                     outputs="text"
                     , title="English to Latin Translator"
                    )

if __name__ == "__main__":
    iface.launch()

