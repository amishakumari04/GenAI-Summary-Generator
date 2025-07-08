from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from backend.utils import read_pdf, read_txt, summarize_text
from backend.challenge import generate_challenge_questions
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_doc(file: UploadFile = File(...)):
    filename = file.filename
    file_location = f"uploads/{filename}"

    with open(file_location, "wb") as f:
        f.write(await file.read())

    if filename.endswith(".pdf"):
        text = read_pdf(file_location)
    elif filename.endswith(".txt"):
        text = read_txt(file_location)
    else:
        return {"error": "Unsupported file format"}

    summary = summarize_text(text)

    return {
        "filename": filename,
        "content": text,
        "summary": summary
    }

@app.post("/ask/")
async def ask_question(text: str = Form(...), question: str = Form(...)):
    prompt = f"Answer this question based on the document:\n\n{text[:4000]}\n\nQ: {question}\nA:"
    try:
        res = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}]
        )
        return {"answer": res.choices[0].message.content.strip()}
    except Exception as e:
        return {"answer": f"[ERROR] Failed to generate answer: {str(e)}"}

@app.post("/challenge/")
async def challenge_user(text: str = Form(...)):
    questions = generate_challenge_questions(text)
    return {"challenge": questions}
