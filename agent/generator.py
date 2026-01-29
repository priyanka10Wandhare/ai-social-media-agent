import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"


def generate(topic):
    prompt = f"""
Write a professional, beginner-friendly LinkedIn post.

Topic: {topic}

Tone: clear, concise, informative.
Avoid emojis. Keep it under 120 words.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    result = response.json()
    return result["response"]

