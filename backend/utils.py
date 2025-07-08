import os
from openai import OpenAI
import fitz  # PyMuPDF
from dotenv import load_dotenv

load_dotenv()

# ✅ Azure OpenAI client using new SDK format
client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    default_headers={"api-key": os.getenv("AZURE_OPENAI_API_KEY")},
)

# ✅ Read PDF content
def read_pdf(file_path: str) -> str:
    text = ""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"[ERROR] Failed to read PDF: {str(e)}"

# ✅ Read TXT content
def read_txt(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[ERROR] Failed to read TXT: {str(e)}"

# ✅ Summarize with Azure OpenAI (new SDK syntax + timeout + debug)
def summarize_text(text: str) -> str:
    print("🟡 summarize_text() called...")  # Debug log
    prompt = f"Summarize the following text in less than 150 words:\n\n{text[:3000]}"

    try:
        res = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}],
            timeout=60  # Optional: timeout safety
        )
        print("🟢 Azure response received")
        return res.choices[0].message.content.strip()
    except Exception as e:
        print(f"🔴 ERROR in summarize_text: {str(e)}")
        return f"[ERROR] Summary failed: {str(e)}"
import os
from openai import OpenAI
import fitz  # PyMuPDF
from dotenv import load_dotenv

load_dotenv()

# ✅ Azure OpenAI client using new SDK format
client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    default_headers={"api-key": os.getenv("AZURE_OPENAI_API_KEY")},
)

# ✅ Read PDF content
def read_pdf(file_path: str) -> str:
    text = ""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return f"[ERROR] Failed to read PDF: {str(e)}"

# ✅ Read TXT content
def read_txt(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"[ERROR] Failed to read TXT: {str(e)}"

# ✅ Summarize with Azure OpenAI (new SDK syntax + timeout + debug)
def summarize_text(text: str) -> str:
    print("🟡 summarize_text() called...")  # Debug log
    prompt = f"Summarize the following text in less than 150 words:\n\n{text[:3000]}"

    try:
        res = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}],
            timeout=60  # Optional: timeout safety
        )
        print("🟢 Azure response received")
        return res.choices[0].message.content.strip()
    except Exception as e:
        print(f"🔴 ERROR in summarize_text: {str(e)}")
        return f"[ERROR] Summary failed: {str(e)}"
