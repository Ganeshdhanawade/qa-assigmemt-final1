from fastapi import FastAPI, UploadFile, Form
from app.routes import query_documnet, upload_document

app = FastAPI()

@app.post("/upload/")
def upload(file: UploadFile):
    return upload_document(file)

@app.get("/query/")
def query(query: str = Form(...)):
    return query_documnet(query)

