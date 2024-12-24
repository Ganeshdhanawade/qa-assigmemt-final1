from app.utils import parse_document, get_embedding
from vectorstore.store import VectorStore
from models.inference import QueryModel

store = VectorStore()
model = QueryModel()

def upload_document(file):
    chunks = parse_document(file)
    embeddings = get_embedding(chunks)
    store.save_embeddings(embeddings,chunks)
    return {"message": "Document processed and store"}

def quary_document(query):
    top_chunks = store.search(query)
    if not top_chunks:
        return {'answer': "I don't know the answer."}
    response = model.answer_query(query, top_chunks)
    return {"answer": response}