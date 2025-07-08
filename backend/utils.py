import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def read_pdf(file_path: str) -> str:
    text = ""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"[ERROR] Failed to read PDF: {str(e)}"

def read_txt(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[ERROR] Failed to read TXT: {str(e)}"

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following text in less than 150 words:\n\n{text[:3000]}"
    try:
        res = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}],
            timeout=60
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] Summary failed: {str(e)}"
