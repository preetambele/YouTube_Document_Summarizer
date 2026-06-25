# YouTube / Document Summarizer

A Streamlit web app that takes a **YouTube video URL** or a **PDF document** and produces an AI‑powered summary using **LangChain** and **Google Gemini** (free tier). All embeddings are generated online via the Google Generative AI API – no local model downloads.

## ✨ Features

- **YouTube Transcript Summarization** – Paste a YouTube link, the transcript is automatically fetched and summarised.
- **PDF Summarization** – Upload any PDF and get a concise, comprehensive summary.
- **Online Embeddings** – Uses Google’s `embedding-001` (free, online), no GPU or large downloads needed.
- **Free LLM** – Summarization powered by `gemini-1.5-flash` (free tier).
- **Modular Code** – Clean separation: loaders, text splitting, embedding + vector store, and the Streamlit UI.
- **Easy to Extend** – Add more document types or switch to another free embedding/LLM provider.

## 🚀 Getting Started

### 1. Clone / Download the Code
Copy the whole `youtube_document_summarizer` folder to your local machine.

### 2. Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate