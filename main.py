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
    # Validation
    if len(data.text) > 280:
        raise HTTPException(status_code=400, detail="Text must be 280 characters or less")
    
    # Idempotency
    if idempotency_key:
        if idempotency_key in idempotency_store:
            return idempotency_store[idempotency_key]
        
    record = {
        "id": str(uuid.uuid4()),
        "text": data.text
    }

    texts_db.append(record)

    if idempotency_key:
        idempotency_store[idempotency_key] = record

    return record

# RETRIVING TEXTS
@app.get("/texts")
def texts(contains: Optional[str] = None):
    if contains:
        return [
            t for t in texts_db
            if contains.lower() in t["text"].lower()
        ]
    return texts_db
