import torch
import gradio as gr
import json

model_path = ("Models/models--facebook--nllb-200-distilled-600M/snapshots"
"/f8d333a098d19b4fd9a8b18f94170487ad3f821d")
# Use a pipeline as a high-level helper
from transformers import pipeline

# pipe = pipeline("translation", model="facebook/nllb-200-distilled-600M")
text_translator = pipeline("translation", model=model_path, torch_dtype=torch.float16)

# Load the JSON data
with open('language.json', "r", encoding="utf-8") as file:
     languages = json.load(file)

def get_FLORES_200_code_from_language(language):
    for entry in languages:
        if entry["Language"].lower() == language.lower():
            return entry["FLORES-200 code"]

        # If not found
    return "Language not found in database."


def translate_text(text, destination_language):
        #text = "hello Friends, how are you doing today?"
        dest_code = get_FLORES_200_code_from_language(destination_language)
        translations = text_translator(text, src_lang="eng_Latn", tgt_lang=dest_code)
        return translations[0]['translation_text'] 

languages_list = [
  "Acehnese (Arabic script)", "Acehnese (Latin script)", "Mesopotamian Arabic", "Ta'izzi-Adeni Arabic",
  "Tunisian Arabic", "Afrikaans", "South Levantine Arabic", "Akan", "Amharic", "North Levantine Arabic",
  "Modern Standard Arabic", "Modern Standard Arabic (Romanized)", "Najdi Arabic", "Moroccan Arabic",
  "Azerbaijani", "Belarusian", "Bengali", "Bulgarian", "Catalan", "Cebuano", "Czech", "Welsh", "Danish",
  "German", "Greek", "English", "Spanish", "Persian", "French", "Gujarati", "Hebrew", "Hindi", "Hungarian",
  "Indonesian", "Italian", "Japanese", "Kannada", "Kazakh", "Korean", "Malayalam", "Marathi", "Nepali",
  "Odia", "Pashto", "Punjabi", "Russian", "Sanskrit", "Sinhala", "Tamil", "Telugu", "Thai", "Turkish",
  "Ukrainian", "Urdu", "Vietnamese", "Chinese (Simplified)", "Chinese (Traditional)"
]

gr.close_all()

demo = gr.Interface(
    fn=translate_text,
    inputs=[gr.Textbox(label="Enter text in English", lines=6, placeholder="Type something to translate..."), gr.Dropdown(choices=languages_list,label="🌐 Select Target Language")],
    outputs=[gr.Textbox(label="🌟Translated text", lines=4)],
    title=" VersaLingo - Multi-Lingual Text Translator 🌍",
    description="Easily translate English text into 50+ global languages using the **NLLB-200 distilled model** powered by Meta AI.",
)

demo.launch()



