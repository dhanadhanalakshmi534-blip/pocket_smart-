import os
from google import genai
from dotenv import load_dotenv

# This securely loads your API key from your .env file
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the NEW Google GenAI SDK
client = genai.Client(api_key=API_KEY)

def get_ai_recommendation(prompt: str):
    """Sends the prompt to Gemini and returns the HTML formatted response."""
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"<p>Error connecting to AI: {str(e)}</p>"