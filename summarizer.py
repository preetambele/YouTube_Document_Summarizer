# summarizer.py
import os
from dotenv import load_dotenv
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma

load_dotenv()


def get_llm():
    """Return Google Gemini LLM (free tier)."""
   
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env")
    return ChatGoogleGenerativeAI( 
        model='gemini-2.5-flash',
        google_api_key=api_key,
        temperature=0   )

def get_embeddings():
    """Return HuggingFace online embeddings (free, no local models)."""
    from langchain_huggingface import HuggingFaceEndpointEmbeddings
    api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not api_token:
        raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in .env")
    return HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=api_token
    )

def create_vectorstore(texts) -> Chroma:
    """Create vector store using HuggingFace online embeddings."""
    embeddings = get_embeddings()
    return Chroma.from_documents(texts, embeddings)

def get_summary(vectorstore: Chroma) -> str:
    """Summarise using Google Gemini and retrieved chunks."""
    llm = get_llm()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

    prompt_template = """You are an expert summarizer. Based on the following context, provide a comprehensive summary. Include key points and main ideas.

Context:
{context}

Summary:"""
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context"])

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPT}
    )
    result = chain.invoke({"query": "Summarize the content"})
    return result['result']
