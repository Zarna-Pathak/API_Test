# Text API (FastAPI)

## Overview

A simple REST API built using **Python and FastAPI**.
It accepts short text messages, stores them in memory, retrieves them, supports search, validates input, and safely handles duplicate POST requests using an idempotency key.

---

## Tech Stack

* Python 3
* FastAPI
* Uvicorn

---

## Setup & Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### POST /texts

* Accepts a text message in JSON body
* Supports optional `Idempotency-Key` header
* Stores text in memory
* Returns the created record with a unique ID

**Request Body**

```json
{ "text": "Hello world" }
```

**Success Response**

```json
{ "id": "uuid", "text": "Hello world" }
```

---

### GET /texts

* Returns all stored texts

---

### GET /texts?contains=word

* Returns only texts containing the given word
* Case-insensitive search

---

## Error Handling & Validation

* Rejects empty text input (empty or whitespace-only)
* Enforces maximum text length of 280 characters
* Returns 400 for validation errors with clear messages
* Handles invalid or missing request bodies via FastAPI/Pydantic
* Prevents duplicate POST requests using idempotency
* Returns 409 Conflict if the same Idempotency-Key is reused with different text

---

## Idempotency Handling

* `POST /texts` supports `Idempotency-Key` header
* Same key + same text → returns previous response
* Same key + different text → returns 409 Conflict
* Prevents duplicate records on retries or network failures

---

## AI Usage Disclosure

### 1. What I used AI for

* Understanding FastAPI concepts (request body, headers, query parameters)
* Learning idempotency behavior in REST APIs
* Clarifying Python concepts like decorators, BaseModel, and UUID
* Structuring endpoint logic correctly
* Improving validation and error handling
* Writing and refining README content

---

### 2. Prompts used

1. “Guide me to build a simple API using Python and FastAPI”
2. “Explain BaseModel in FastAPI in simple terms”
3. “Explain decorators in FastAPI with examples”
4. “How does Idempotency-Key work in REST APIs?”
5. “Help me write a clear README for this task”

---

### 3. What I changed manually

* Wrote and structured the final API code
* Implemented validation logic for empty and long text
* Designed idempotency behavior and conflict handling
* Simplified logic to keep it beginner-friendly
* Edited README for clarity and correctness

---

### 4. How I verified correctness

* Tested all endpoints using FastAPI Swagger UI
* Verified empty text and length validation errors
* Tested idempotency behavior with repeated POST requests
* Tested conflict handling with same key and different text
* Tested search functionality with different cases

---

## Interview Questions

### Why did you choose this framework?

* Lightweight and easy to learn
* Built-in validation using Pydantic
* Automatic interactive API documentation

---

### What are 3 failure cases you handled?

1. Empty or whitespace-only text input
2. Text exceeding 280 characters
3. Duplicate POST requests using the same Idempotency-Key

---

### If this API had 10,000 users/day, what would break first?

* In-memory storage would not scale
* Data would be lost on server restart

---

### What would you improve next?

* Use a persistent database (PostgreSQL or similar)

---
