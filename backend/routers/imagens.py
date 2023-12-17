from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import PIL.Image
import os


router = APIRouter()

# Diretório para salvar as imagens
image_directory = "storage"
os.makedirs(image_directory, exist_ok=True)


def resize_image(image_path, output_path, size=(300, 300)):
    """Redimensiona a imagem para o tamanho desejado."""
    with open(image_path, "rb") as f:
        image = PIL.Image.open(f)

    image.thumbnail(size)
    image.save(output_path)


@router.post("/storage")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        if not file.content_type.startswith("image"):
            raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem.")

        # Salva a imagem no diretório original
        original_file_path = os.path.join(image_directory, file.filename)
        with open(original_file_path, 'wb') as f:
            f.write(file.file.read())

        # Redimensiona a imagem
        resized_file_path = os.path.join(image_directory, f"resized_{file.filename}")
        resize_image(original_file_path, resized_file_path)

        return JSONResponse(content={"message": "Imagem salva e tratada com sucesso.", "file_path": resized_file_path})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    