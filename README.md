# 📄 YouTube & Document Summarizer

### AI-Powered Content Summarization using Google Gemini + LangChain

An AI-powered **YouTube + PDF Summarization System** built using **LangChain, Google Gemini, HuggingFace Embeddings, and Streamlit**.

This application converts **long videos and lengthy documents into concise, readable summaries** using Retrieval-Augmented Generation (RAG).

Upload a PDF or paste a YouTube link — and receive an AI-generated summary in seconds.

---

# 🚀 Features

### 🎥 YouTube Video Summarization

Paste any YouTube URL and automatically:

* Extract transcript
* Process content
* Generate AI summary

---

### 📑 PDF Summarization

Upload PDF documents and:

* Extract text
* Split into chunks
* Generate structured summaries

---

### 🧠 LLM-Powered Summaries

Uses:

* Google Gemini 2.5 Flash
* LangChain Retrieval Pipeline

---

### 🔍 Retrieval-Augmented Generation (RAG)

Pipeline includes:

* Text chunking
* Embedding generation
* Vector storage
* Retrieval-based summarization

---

### ⚡ Online Embeddings

Uses:

* HuggingFace Endpoint Embeddings
* No local model downloads

---

### 🎨 Streamlit Interface

Simple UI with:

* YouTube mode
* PDF upload mode
* Summary display

---

# 🏗️ Architecture

```text
User Input
(YouTube / PDF)

      │
      ▼

Load Content
Transcript / PDF Reader

      │
      ▼

Text Splitting
RecursiveCharacterTextSplitter

      │
      ▼

Generate Embeddings
HuggingFace Endpoint

      │
      ▼

Store Vectors
Chroma

      │
      ▼

Retriever

      │
      ▼

Google Gemini

      │
      ▼

Generated Summary
```

---

# 🧰 Tech Stack

| Layer          | Technology              |
| -------------- | ----------------------- |
| Frontend       | Streamlit               |
| Language       | Python                  |
| Framework      | LangChain               |
| LLM            | Google Gemini 2.5 Flash |
| Embeddings     | HuggingFace Endpoint    |
| Vector Store   | Chroma                  |
| YouTube Loader | youtube-transcript-api  |
| PDF Processing | PyPDF                   |
| Environment    | Dotenv                  |

---

# 📂 Project Structure

```bash
YouTube_Document_Summarizer/

├── app.py
├── loaders.py
├── summarizer.py
├── utils.py
├── requirements.txt
└── README.md
```


# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/preetambele/YouTube_Document_Summarizer.git

cd YouTube_Document_Summarizer
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create `.env`

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

HUGGINGFACEHUB_API_TOKEN=YOUR_HUGGINGFACE_TOKEN
```

---

# ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🎥 Summarize YouTube Video

1. Select **YouTube Link**
2. Paste video URL

Example:

```text
https://www.youtube.com/watch?v=example
```

3. Click:

```text
✨ Summarize
```

Output:

```text
Generated video summary
```

---

# 📄 Summarize PDF

1. Select **PDF Upload**
2. Upload document
3. Click summarize

Output:

```text
AI-generated document summary
```

---

# 🔄 Processing Flow

### Content Loading

**YouTube**
→ Transcript Extraction

**PDF**
→ Page Text Extraction

↓

### Chunking

Split content using:

```text
chunk_size = 1000
overlap = 200
```

↓

### Embeddings

Generate semantic vectors

↓

### Retrieval

Retrieve top relevant chunks

↓

### Summarization

Generate final summary with Gemini

---

# 📊 Example Output

```text
Topic:
Large Language Models

Summary:

This content explains the
evolution of LLMs,
their architecture,
applications,
and future trends.

Key Insights:
- Transformer models
- Retrieval systems
- Fine tuning
```

---

# 🔮 Future Enhancements

* Multi-language Summaries
* PDF Export
* Summary History
* Chat with Documents
* Audio Upload Support
* Batch Processing
* Timestamped YouTube Summaries
* LangGraph Integration

---

# 🛣️ Roadmap

* [x] YouTube Summarization
* [x] PDF Summarization
* [x] Gemini Integration
* [x] Chroma Vector Store
* [ ] Chat Interface
* [ ] Export Features
* [ ] Multi-document Support
* [ ] Cloud Deployment

---

# 🤝 Contributing

```bash
Fork Repository

Create Feature Branch

Commit Changes

Open Pull Request
```

---

# ⭐ Support

If you found this useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

---

# 👨‍💻 Author

**Preetam Bele**

AI Engineer • LLM Developer • RAG • Generative AI • LangChain


