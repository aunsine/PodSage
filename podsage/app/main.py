from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/search")
def semantic_search(query: str = Query(...)):
    embedding = requests.post("http://ml_service:5000/embed", json={"text": query}).json()
    # TODO: Send embedding to ElasticSearch and return ranked episodes
    return {"query_vector": embedding}
