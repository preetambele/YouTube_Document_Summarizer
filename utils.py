# utils.py
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(docs, chunk_size=1000, chunk_overlap=200):
    """
    Split a list of documents into smaller chunks for better embedding and retrieval.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_documents(docs)