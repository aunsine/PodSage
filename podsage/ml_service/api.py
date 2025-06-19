from fastapi import FASTAPI, Request
from sentence_transformers import SentenceTransformer

app = FASTAPI()
model = SentenceTransformer("all-MiniLM-L6_v2")

@app.post("/embed")
async def embed(request: Request):
    body = await request.json()
    text = body.get("text","")
    embedding = model.encode(text).tolist()
    return embedding

