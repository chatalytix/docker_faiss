from fastapi import FastAPI
from app.search import setup_faiss, search_faiss
from app.db import get_metadata

app = FastAPI()

# Initialize FAISS index
faiss_index = setup_faiss()

@app.post("/search")
def search_vectors(query_vector: list, top_k: int = 5):
    """
    Perform a FAISS vector search and enrich the results with MongoDB metadata.
    """
    search_results = search_faiss(faiss_index, query_vector, top_k=top_k)
    enriched_results = get_metadata(search_results)
    return {"results": enriched_results}
