from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def rewrite_document(text):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": f"""
Rewrite this document in a professional style.

{text}
"""
            }
        ]
    )

    return response.choices[0].message.content