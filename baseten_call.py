import os
import requests

api_key = os.environ.get("BASETEN_API_KEY")
url = "https://inference.baseten.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

payload = {
    "model": "meta-models/muse-spark-open-1026",
    "messages": [
        {
            "role": "user",
            "content": "Say hello to Pocket Muse in one short sentence, and say which model you are.",
        }
    ],
}

response = requests.post(
    url,
    headers=headers,
    json=payload,
)

print("HTTP status:", response.status_code)
data = response.json()
try:
    print("ANSWER:", data["choices"][0]["message"]["content"])
except Exception:
    print(data)
