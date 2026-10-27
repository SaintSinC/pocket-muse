"""Pocket Muse Brain - Skill 1: Ask -> Think -> Draw.

Pipeline (built during the Meta Global AI Developer Hackathon, Oct 27 2026):
  1. Muse Spark 1.3 (Meta Model API) writes a one-line spoken fact about the
     subject, plus an image prompt.
  2. Muse Image 1.0 (Meta Model API) draws the picture.
  3. The script prints the spoken line and the public image URL; the gadget's
     round screen then displays the URL (display.draw_url).

Usage:  python3 brain.py "a tiger"
Keys:   MODEL_API_KEY in the environment (never printed).
"""
import os
import sys

import requests

API_KEY = os.environ.get("MODEL_API_KEY")
BASE = "https://api.meta.ai/v1"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

SYSTEM = (
    "You are the Brain of Pocket Muse, a pocket voice companion. "
    "Reply in exactly two parts and nothing else: first ONE short fun-fact "
    "sentence about the subject (max 20 words, plain text, no markdown), "
    "then a newline, then a line beginning with IMAGE: followed by a vivid "
    "image-generation prompt (subject centered, bright colors, simple "
    "background, no text in the image)."
)


def ask_spark(subject):
    payload = {
        "model": "muse-spark-1.3",
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": subject},
        ],
    }
    r = requests.post(f"{BASE}/chat/completions", headers=HEADERS, json=payload)
    print("Spark HTTP status:", r.status_code)
    data = r.json()
    text = data["choices"][0]["message"]["content"]
    if "IMAGE:" in text:
        answer, image_prompt = text.split("IMAGE:", 1)
        return answer.strip(), image_prompt.strip()
    return text.strip(), subject


def draw(image_prompt):
    payload = {
        "model": "muse-image-1.0",
        "prompt": image_prompt,
        "n": 1,
        "size": "1024x1024",
        "response_format": "url",
        "output_format": "jpeg",
    }
    r = requests.post(f"{BASE}/images/generations", headers=HEADERS, json=payload)
    print("Image HTTP status:", r.status_code)
    data = r.json()
    return data["data"][0]["url"]


def main():
    subject = " ".join(sys.argv[1:]) or "a red panda"
    print("Subject:", subject)
    answer, image_prompt = ask_spark(subject)
    print("ANSWER:", answer)
    print("IMAGE PROMPT:", image_prompt)
    url = draw(image_prompt)
    print("IMAGE_URL:", url)
    try:
        img = requests.get(url)
        with open("last_image.jpg", "wb") as f:
            f.write(img.content)
        print("Saved a copy as last_image.jpg")
    except Exception as e:
        print("Local save skipped:", e)


if __name__ == "__main__":
    main()
