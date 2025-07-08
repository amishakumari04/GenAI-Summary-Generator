import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def generate_challenge_questions(text: str) -> str:
    prompt = f"""
Generate 3 logic-based or comprehension questions based on the following text. Format:
Q1: ...
A1: ...
Explanation: ...

TEXT:
{text[:4000]}
"""

    try:
        res = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] Failed to generate challenge: {str(e)}"
