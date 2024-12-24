from pymilvus import connections, Collection, CollectionSchema,FieldSchema, DataType
from app.utils import get_embedding

class VectorStore:
    #create the database
    def __init__(self):
        connections.connect("default", host="localhost", port = 19530)
        fields = [
            FieldSchema(name="embedding",dtype=DataType.FLOAT_VECTOR,dim = 768),
            FieldSchema(name="chunk",dtype=DataType.VARCHAR,max_length =400),
        ]
        schema = CollectionSchema(fields, "Document storage")
        self.collection = Collection('document_chunk', schema=schema)
        if not self.collection.is_empty:
            self.collection.load()

    #save the embedding inside database
    def save_embeddings(self, embeddings, chunks):
        entities = [
            [emb.tolist() for emb in embeddings], #insert embedding
            chunks, #insert test
        ]
        self.collection.insert(entities)

    #similarity search according to serach quary in vectorstore
    def search(self, query):
        query_embedding = get_embedding([query])[0]
        results = self.collection.search(
            data=[query_embedding.tolist()],
            anns_field="embedding",
            param={"metric_type":"IP","params":{"nprobe":10}},
            limit=3,
            expr=None
        )
        top_chunks = [hit.entity.get("chunk") for hit in results[0]]
        return top_chunks

    
