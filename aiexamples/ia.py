import requests

from api import API_KEY

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + API_KEY

def generate_celebrity_comment(image_base64):
    prompt = (
        "Bu fotoğrafta görülen kişiye, bir ünlü hayranı gibi sıcak ve samimi bir Instagram yorumu yazar mısın? "
        "Yorum kısa, eğlenceli ve pozitif olmalı. Emoji kullanılabilir."
    )
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {"inlineData": {"mimeType": "image/jpeg", "data": image_base64}}
                ]
            }
        ]
    }
    response = requests.post(url, json=data)
    try:
        resp_json = response.json()
        print("API Response:", resp_json)   # << Bunu ekle!
        return resp_json["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("API Response:", response.text)
        raise e


import base64

# 1. Fotoğraf dosyasını binary modda aç
with open("pic.jpg", "rb") as image_file:
    image_bytes = image_file.read()

# 2. Base64'e çevir
image_base64 = base64.b64encode(image_bytes).decode("utf-8")
generate_celebrity_comment(image_base64)