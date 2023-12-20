import os

import requests

url = "https://v2.api.audio/speech/tts/sync"

headers = {
    "Content-Type": "application/json",
    "x-api-key": os.getenv("AFLR_KEY"),
}


def tts(text: str, voice: str = "coco"):
    payload = {
        "sampling_rate": "24000",
        "bitrate": "192",
        "speed": 1,
        "text": text,
        "voice": voice,
        "url": True,
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()["data"]["url"]
