# app.py
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

from loaders import load_youtube_transcript, load_pdf
from utils import split_documents
from summarizer import create_vectorstore, get_summary

st.set_page_config(page_title="YouTube & PDF Summarizer", layout="wide")
st.title("📄 YouTube / Document Summarizer")
st.markdown(
    "Paste a **YouTube link** or **upload a PDF** – get an AI‑generated summary using "
    "Google Gemini (LLM) + HuggingFace (online embeddings)."
)

# Check that both API keys are set (they're now used internally by summarizer.py)
if not os.getenv("GOOGLE_API_KEY"):
    st.warning("Please set GOOGLE_API_KEY in your .env file to use the free Gemini LLM.")
if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    st.warning("Please set HUGGINGFACEHUB_API_TOKEN in your .env file for free online embeddings.")
    st.stop()   # Stop if embeddings API key missing

input_type = st.sidebar.radio("Select Input Type", ["YouTube Link", "PDF Upload"])

if input_type == "YouTube Link":
    video_url = st.text_input("🎥 Enter YouTube Video URL:")
    if video_url:
        if st.button("✨ Summarize"):
            with st.spinner("Fetching transcript and generating summary..."):
                try:
                    docs = load_youtube_transcript(video_url)
                    texts = split_documents(docs)
                    vectorstore = create_vectorstore(texts)          # ✅ No api_key argument
                    summary = get_summary(vectorstore)               # ✅ No api_key argument
                    st.subheader("📝 Summary")
                    st.write(summary)
                except Exception as e:
                    st.error(f"❌ Error: {e}")

else:
    pdf_file = st.file_uploader("📤 Upload a PDF file", type="pdf")
    if pdf_file is not None:
        if st.button("✨ Summarize"):
            with st.spinner("Reading PDF and generating summary..."):
                try:
                    docs = load_pdf(pdf_file)
                    texts = split_documents(docs)
                    vectorstore = create_vectorstore(texts)
                    summary = get_summary(vectorstore)
                    st.subheader("📝 Summary")
                    st.write(summary)
                except Exception as e:
                    st.error(f"❌ Error: {e}")
                    