import faiss
import numpy as np

def create_index(dataset, embedding_dim=768):
    embeddings = np.array(dataset["embeddings"]).astype(np.float32)
    embedding_dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(embedding_dim)
    index.add(embeddings)
    
    faiss.write_index(index, "/data/document_index.faiss")
    dataset.add_faiss_index("embeddings", custom_index=index)
    
    return index
