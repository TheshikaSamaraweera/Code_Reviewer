# llm_client.py

import requests
import os


class LLMClient:
    def __init__(self, model_name="gemini-2.0-flash"):
        self.api_key = os.getenv("GEMINI_API_KEY")  # API key env variable
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={self.api_key}"
        self.headers = {"Content-Type": "application/json"}

    def send_prompt(self, prompt: str) -> str:
        """
        Sends the prompt to Gemini and returns the response text.
        """
        data = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(self.url, headers=self.headers, json=data)

        if response.status_code != 200:
            raise Exception(f"LLM API Error: {response.status_code} - {response.text}")

        response_json = response.json()
        return response_json['candidates'][0]['content']['parts'][0]['text']
