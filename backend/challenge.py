import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"

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
        res = openai.ChatCompletion.create(
            engine=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        return f"[ERROR] Failed to generate challenge: {str(e)}"
