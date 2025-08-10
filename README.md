# 📄 PDF Summarizer using Google Gemini AI

An AI-powered tool that extracts text from PDFs and generates **clear, concise summaries** using **Google's Gemini API**.

---

## ✨ Features
- 📂 **PDF & Text Support** – Summarize `.pdf` or `.txt` files  
- ⚡ **Gemini AI** – Leverages `gemini-1.5-flash` for high-quality summaries  
- 📏 **Smart Chunking** – Handles large documents in 400-word sections  
- 📋 **Bullet-Point Output** – Prioritized from most important to least important  
- 🗂 **Clean Output** – Saves summaries in `outputs/summary.txt`

---

## 📦 Installation
```bash
# 1. Clone repository
git clone https://github.com/rajnishkumar1906/PDF-Summarizer.git
cd PDF-Summarizer

# 2. Create virtual environment
python -m venv venv
# Activate: .\venv\Scripts\activate  (Windows)
#           source venv/bin/activate (Mac/Linux)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add API key to .env
echo GEMINI_API_KEY=your_api_key_here > .env