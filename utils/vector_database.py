import faiss
import numpy as np

# Initialize FAISS index (for example using a 128-dimensional space)
dimension = 128  # Dimensionality of the embedding vectors
index = faiss.IndexFlatL2(dimension)

def add_vectors_to_store(vector_store, embeddings):
    """Add embeddings to FAISS vector store."""
    embeddings = np.array(embeddings).astype('float32')
    vector_store.add(embeddings)

def search_vectors(vector_store, query_embedding, k=5):
    """Search for the top k most similar vectors."""
    query_embedding = np.array(query_embedding).astype('float32')
    distances, indices = vector_store.search(query_embedding, k)
    return distances, indices
