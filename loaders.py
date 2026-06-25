# loaders.py
import tempfile
import os
import re
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document

def extract_video_id(url: str) -> str:
    """Extract the 11-character YouTube video ID from various URL formats."""
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL. Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def load_youtube_transcript(video_url: str):
    video_id = extract_video_id(video_url)

    # ✅ Instantiate the API client, then call fetch()
    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    full_text = " ".join([entry.text for entry in transcript])
    return [Document(page_content=full_text, metadata={"source": video_url})]

def load_pdf(file):
    """Load text from an uploaded PDF file using pypdf."""
    from pypdf import PdfReader

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.read())
        tmp_path = tmp.name

    reader = PdfReader(tmp_path)
    docs = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            docs.append(Document(page_content=text, metadata={"page": i+1, "source": file.name}))
    os.unlink(tmp_path)
    return docs