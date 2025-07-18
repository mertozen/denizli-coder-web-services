from fastapi import FastAPI, File, UploadFile
import shutil
import os

from ia import generate_celebrity_comment

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        return {"error": "Sadece resim dosyaları yükleyebilirsiniz."}

    import base64
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 1. Fotoğraf dosyasını binary modda aç
    with open(file_location, "rb") as image_file:
        image_bytes = image_file.read()

    # 2. Base64'e çevir
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    return {"message": generate_celebrity_comment(image_base64), "file_path": file_location}
