import os
import requests

api_key = os.environ.get("MODEL_API_KEY")
url = "https://api.meta.ai/v1/responses"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

payload = {
    "model": "muse-wonder-1.0",
    "input": [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Write a script that randomly generates a haiku about Meta, and explain your reasoning behind what script language you would choose."
                }
            ]
        }
    ],
    "stream": False,
}

response = requests.post(
    url,
    headers=headers,
    json=payload,
)

print(response.json())
