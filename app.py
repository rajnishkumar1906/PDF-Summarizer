import streamlit as st
import os
from utils.pdf_reader import extract_text_from_pdf
from utils.text_processor import clean_text, chunk_text
from utils.summarizer import 

st.markdown(
    """
    <style>
    body, .block-container {
        background: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
        min-height: 80vh;
        color: #222222;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding-top: 50px;
        padding-bottom: 50px;
    }
    .css-1v0mbdj h1 {
        text-align: center;
        font-weight: 900;
        font-size: 3.5rem;
        color: #003366;
        margin-bottom: 10px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.15);
    }
    .css-1v0mbdj p {
        text-align: center;
        font-size: 1.3rem;
        color: #0a4a8f;
        margin-bottom: 50px;
        font-weight: 700;
    }
    .stFileUploader, .stButton {
        background: #ffffffee !important;
        border-radius: 20px !important;
        box-shadow: 0 12px 25px rgba(0,0,0,0.1);
        padding: 25px !important;
        margin-bottom: 40px !important;
    }
    button[kind="primary"] {
        background-color: #0c3c91 !important;
        color: white !important;
        font-weight: 700 !important;
        padding: 15px 35px !important;
        border-radius: 15px !important;
        box-shadow: 0 8px 20px rgba(12, 60, 145, 0.5);
        transition: background-color 0.3s ease;
    }
    button[kind="primary"]:hover {
        background-color: #062a64 !important;
        cursor: pointer;
    }
    .stInfo, .stSuccess, .stError {
        border-radius: 15px;
        padding: 20px 25px;
        margin-bottom: 30px;
        font-weight: 700;
        font-size: 1.1rem;
    }
    .stInfo {
        background-color: #cfe4fc !important;
        color: #0c3c91 !important;
    }
    .stSuccess {
        background-color: #d4f1dc !important;
        color: #0a8f4a !important;
    }
    .stError {
        background-color: #f9d6d5 !important;
        color: #c9302c !important;
    }
    .summary-card {
        background: white;
        border-radius: 30px;
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 14px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #111827;
    }
    .summary-card:hover {
        transform: scale(1.05);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    .summary-header {
        font-weight: 900;
        font-size: 1.5rem;
        color: #0c3c91;
        margin-bottom: 18px;
        border-bottom: 3px solid #0c3c91;
        padding-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("SharpSummary")
st.write("Upload your PDF and get an AI-powered summary instantly!")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    temp_pdf_path = "temp_uploaded.pdf"
    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("🔍 Extracting text from PDF...")
    raw_text = extract_text_from_pdf(temp_pdf_path)

    if raw_text:
        st.success("✅ Text extracted successfully!")
        st.info("🧹 Cleaning and chunking text...")

        cleaned_text = clean_text(raw_text)
        chunks = chunk_text(cleaned_text, max_words=400)

        st.write(f"🔢 Text split into **{len(chunks)}** chunks.")

        st.info("🤖 Summarizing chunks...")
        progress_bar = st.progress(0)

        full_summary_text = ""

        for i in range(len(chunks)):
            summary = summarize_chunk(chunks[i])
            full_summary_text += f"--- Summary for Chunk {i+1} ---\n{summary}\n\n"
            st.markdown(
                f"""
                <div class="summary-card">
                    <div class="summary-header">Summary for Chunk {i+1}</div>
                    <div>{summary}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            progress_bar.progress((i + 1) / len(chunks))

        progress_bar.empty()

        # Download button for summary text
        st.download_button(
            label="📥 Download Summary as TXT",
            data=full_summary_text,
            file_name="sharpsummary.txt",
            mime="text/plain",
        )

    else:
        st.error("⚠️ Failed to extract text from the PDF.")
else:
    st.info("Please upload a PDF file to get started.")
