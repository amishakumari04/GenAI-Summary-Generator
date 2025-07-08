# 🧠 GenAI Smart Research Assistant

A full-stack AI-powered assistant for summarizing research documents, answering questions, and generating challenge questions from PDF/TXT files.

> Powered by **Azure OpenAI**, built using **FastAPI** (backend) and **Streamlit** (frontend).

---

## 📁 Project Structure


---

## 🧰 Features

- 📄 Upload `.pdf` or `.txt` research documents
- ✨ Auto-summarize content using Azure OpenAI
- ❓ Ask custom questions from document
- 💡 Generate "Challenge Me" logic-based Q&A
- 🎛️ Toggle between modes: Free-form or challenge

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/genai-assistant.git
cd genai-assistant

---

## 🧰 Features

- 📄 Upload `.pdf` or `.txt` research documents
- ✨ Auto-summarize content using Azure OpenAI
- ❓ Ask custom questions from document
- 💡 Generate "Challenge Me" logic-based Q&A
- 🎛️ Toggle between modes: Free-form or challenge

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/genai-assistant.git
cd genai-assistant
3. Install Dependencies
bash
pip install -r requirements.txt

4. Configure Azure API Keys
Create a .env file in the root directory:

.env
AZURE_OPENAI_API_KEY=your-azure-api-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-35-turbo
⚠️ Make sure your Azure deployment name matches AZURE_OPENAI_DEPLOYMENT

5. Run the Backend (FastAPI)
bash
uvicorn backend.main:app --reload
Starts the backend at http://localhost:8000

6. Run the Frontend (Streamlit)
bash
cd frontend
streamlit run app.py
Opens app at http://localhost:8501

🖼️ Interface
📄 Upload file (PDF or TXT)

✅ Summary auto-displayed

💬 Ask custom questions

🧠 Challenge Me: Get logic/comprehension questions

✅ Requirements
All dependencies are listed in requirements.txt. Major packages:

fastapi

uvicorn

python-multipart

openai (Azure-compatible)

python-dotenv

requests

streamlit

PyMuPDF (for reading PDFs)

🧠 Powered By
Azure OpenAI (GPT-3.5 Turbo or GPT-4)

FastAPI

Streamlit

PyMuPDF

📬 Feedback / Issues?
Raise an issue or drop feedback on your GitHub repo.

🏑 License
MIT License. Use freely and share openly.

vbnet
Let me know if you want this as a downloadable file or want to add badges, images, or examples.



