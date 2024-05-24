from datasets import Dataset
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

def create_dataset(document_info):
    documents = [{"title": "Document", "text": document_info}]
    dataset = Dataset.from_dict({
        "title": [doc["title"] for doc in documents],
        "text": [doc["text"] for doc in documents]
    })
    
    model = SentenceTransformer(f'sentence-transformers/{os.getenv("EMBEDDING_MODEL_NAME")}')
    embeddings = model.encode([doc["text"] for doc in documents])
    
    dataset = dataset.add_column("embeddings", embeddings.tolist())
    dataset = dataset.add_faiss_index(column="embeddings")
    
    return dataset