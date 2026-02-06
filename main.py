from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()

texts_db = []
idempotency_store = {}

class TextInput(BaseModel):
    text : str

# ACCEPTING & STORING TEXT WITH VALIDATIONS AND BASIC ERROR HANDLING
@app.post("/texts")
def create_texts(
    data: TextInput, 
    idempotency_key: Optional[str] = Header(None)
):
    # Empty text validation
    if not data.text or not data.text.strip():
        raise HTTPException(status_code=400, detail="Text must contain at least one non-whitespace character")
    
    # Length Validation
    if len(data.text) > 280:
        raise HTTPException(status_code=400, detail="Text exceeds the maximum length of 280 characters")
    
    # Idempotency handling
    if idempotency_key:
        existing = idempotency_store.get(idempotency_key)
        if existing:
            if existing["request_text"] != data.text:
                raise(HTTPException(status_code=409, detail="This Idempotency-Key was already used for a different text. Please use a new key"))
        
            return idempotency_store[idempotency_key]
        
    record = {
        "id": str(uuid.uuid4()),
        "text": data.text
    }

    texts_db.append(record)

    # Store Idempotency Result
    if idempotency_key:
        idempotency_store[idempotency_key] = {"request_text":data.text, "response": record}

    return record

# RETRIVING TEXTS
@app.get("/texts")
def texts(contains: Optional[str] = None):
    if not contains or not contains.strip():
        raise HTTPException(status_code=400, detail="Query parameter 'contains' is required for search")

    results = [
        t for t in texts_db
        if contains.lower() in t["text"].lower()
    ]

    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No texts found containing '{contains}'"
        )
    return results
    
