import os
from transformers import RagRetriever
from dotenv import load_dotenv
import faiss

load_dotenv()

class RetrieverRag:
    def __init__(self, dataset):
        model_name = os.getenv("MODEL_NAME")
        faiss_document_url = os.path.join(os.path.dirname(__file__), 'data', 'document_index.faiss')
        index_faiss = faiss.read_index(faiss_document_url)
        self.retriever = RagRetriever.from_pretrained(
            model_name,
            index_name="legacy",
            passages_path=faiss_document_url,
            indexed_dataset=dataset,
            index=index_faiss
        )
    
    
    def get_retriever(self):
        return self.retriever