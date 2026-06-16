from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def summarize_document(text):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Summarize this document:\n\n{text}"
    )

    return response.text