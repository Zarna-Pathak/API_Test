# Text Storage API (FastAPI)

## Overview
A simple REST API built using **Python and FastAPI** that accepts short text messages, stores them in memory, retrieves them, supports search, validates input, and handles idempotent POST requests.

---

## Tech Stack

* Python 3
* FastAPI
* Uvicorn
  
---

## Setup & Run
```
pip install fastapi uvicorn
uvicorn main:app --reload
```

API Docs:
``` http://127.0.0.1:8000/docs ```

---

## API Endpoints

### POST /texts
* Accepts a text message in JSON body
* Optional `Idempotency-Key` header supported
* Validates text length (≤ 280 characters)

**Request Body**
``` { "text": "Hello world" } ```

**Error (400)**
``` { "detail": "Text must be 280 characters or less" } ```

---

### GET /texts
* Returns all stored texts

---

### GET /texts?contains=word
* Returns texts containing the given word
* Case-insensitive search

---

## Idempotency Handling
* `POST /texts` supports `Idempotency-Key` header
* Reusing the same key returns the previously created response
* Prevents duplicate text creation on retries

---

## Error Handling & Validation
* Text length validation (≤ 280 characters)
* Missing or invalid request body handled by FastAPI
* Safe handling of duplicate POST requests using idempotency

---

## AI Usage Disclosure

### 1. What I used AI for
* Understanding FastAPI request handling (body, headers, query params)
* Understanding and implementing idempotency logic
* Clarifying Python concepts like decorators, BaseModel, and UUID
* Structuring API endpoints correctly
* Drafting and refining the README structure

---

### 2. Prompts used 
1. “Guide me to build a simple API using Python and FastAPI”
2. “Explain BaseModel in FastAPI in simple terms”
3. “Explain decorators in FastAPI with examples”
4. “How does Idempotency-Key work in REST APIs?”
5. “Help me write a clear README for a FastAPI interview task”

---

### 3. What I changed manually
* Wrote and structured the final API code myself
* Simplified logic to keep it beginner-friendly
* Adjusted validation and error handling to match task requirements
* Edited README content for clarity

---

### 4. How I verified correctness
* Tested all endpoints using FastAPI Swagger UI
* Verified text length validation error response
* Tested repeated POST requests with same Idempotency-Key
* Tested search functionality with different cases

---

## Interview Questions

### Why did you choose this framework?
* Lightweight and easy to set up
* Built-in validation and error handling
* Automatic API documentation

---

### What are 3 failure cases you handled?
1. Text exceeding 280 characters
2. Invalid request body
3. Duplicate POST requests using the same Idempotency-Key

---

### If this API had 10,000 users/day, what would break first?
* In-memory storage would not scale
* Data would be lost on server restart
* Concurrent access could cause inconsistencies

---

### What would you improve next?
* Use a persistent database (PostgreSQL / SQL)

  
