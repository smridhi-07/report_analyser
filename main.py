from pdftoimg import pdf_to_images
from imgtotxt import ocr_slides
from cdai import analysis
import os

from fastapi import FastAPI,File,UploadFile
app=FastAPI()

UPLOAD_DIR = "uploaddir"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
  return {"message":"backend running"}

@app.post("/analyse")
async def analyses( file: UploadFile = File(...) ):
  if file.content_type != "application/pdf":
    return
  
  file_path=os.path.join(UPLOAD_DIR,file.filename)

  with open(file_path, "wb") as buffer:
    buffer.write(file.file.read())

  pdf_to_images(file_path)
  x=ocr_slides()
  s="".join(x)
  
  y=analysis(s)
  return y
  
 