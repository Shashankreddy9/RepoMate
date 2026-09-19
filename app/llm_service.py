import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is not set in the .env file."
    )


client = genai.Client(
    api_key=GEMINI_API_KEY
)


MODEL_NAME = "gemini-3.6-flash"


def generate_answer(prompt: str):
    """
    Generate an answer using Gemini.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text