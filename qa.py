# qa.py

from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def ask_question(document_text, question):

    prompt = f"""
Document:

{document_text}

Answer this question using only the document.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content