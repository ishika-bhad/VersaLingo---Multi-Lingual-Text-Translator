# 🌍 VersaLingo - Multi-Lingual Text Translator

VersaLingo is a **multi-lingual text translator** that converts **English** text into 50+ languages using the **NLLB-200 distilled model** by Meta AI.  
The project is powered by **PyTorch**, **Hugging Face Transformers**, and **Gradio** for a clean, interactive web interface.

---

## 🚀 Features
- Translate English text into 50+ global languages.
- Uses **NLLB-200 distilled model** for high-quality translations.
- Simple **Gradio UI** — paste text, choose a language, and translate instantly.
- Supports FLORES-200 language codes for accurate mapping.

---

## 🛠 Tech Stack
- **Python**
- **PyTorch**
- **Transformers (Hugging Face)**
- **Gradio**

---

## 📂 Project Structure
multi-language-translator/
│── mlt.py # Main application file
│── language.json # Mapping of language names to FLORES-200 codes
│── model/ # Local NLLB-200 distilled model folder
│── requirements.txt # Dependencies


---

## 📦 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/multi-language-translator.git
cd multi-language-translator
---
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
---
###3️⃣ Run the app
```bash
python mlt.py

---
## 🌐 **Supported Languages**
Over 50 global languages including Hindi, Spanish, French, Japanese, Arabic, Korean, and more.

---

## 📜 **License**
This project is licensed under the MIT License.
