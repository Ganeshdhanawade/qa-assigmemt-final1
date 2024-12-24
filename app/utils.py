import torch
from PyPDF2 import PdfReader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer, AutoModel


#split the documnet into the chunks
def parse_document(file):
    """split document into the chunks"""
    reader = PdfReader(file.file)
    text = "".join(page.extract_text() for page in reader.pages)
    
    # recursive text spliter
    splitter = RecursiveCharacterTextSplitter(chunk_size = 350, chunk_overlap = 50)
    chunks = splitter.split_text(text)
    return chunks


#create the embeddings of each chunks
def get_embedding(chunks):
    """ create embedding using hugging face transformer"""
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    embeddings = []
    for chunk in chunks:
        tokens = tokenizer(chunk, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**tokens)
            embeddings.append(outputs.last_hidden_state.mean(dim=1))
    return embeddings