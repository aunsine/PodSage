from fastapi import FastAPI, Request
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.post("/embed")
async def embed(request: Request):
    body = await request.json()
    text = body.get("text", "")
    embedding = model.encode(text).tolist()
    return embedding
