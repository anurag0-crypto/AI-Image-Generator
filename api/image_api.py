import os
import requests

from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError(
        "HF_TOKEN not found. Check .env file."
    )

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

MODEL_URL = (
    "https://router.huggingface.co/"
    "hf-inference/models/"
    "black-forest-labs/FLUX.1-schnell"
)

def generate_image(prompt):

    response = requests.post(
        MODEL_URL,
        headers=HEADERS,
        json={
            "inputs": prompt
        },
        timeout=300
    )

    response.raise_for_status()

    return response.content