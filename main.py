from fastapi import FastAPI, UploadFile, Form
from app.routes import quary_document, upload_document

app = FastAPI()

@app.post("/upload/")
def upload(file: UploadFile):
    return upload_document(file)

@app.get("/query/")
def query(query: str = Form(...)):
    return quary_document(query)

