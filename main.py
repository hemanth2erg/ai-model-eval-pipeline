from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel
import logging

app = FastAPI()

class EvalInput(BaseModel):
    prompt: str
    response: str

@app.post("/evaluate")
def evaluate(input: EvalInput):
    # Placeholder for scoring logic
    return {"hallucination_score": 0.2, "logic_score": 0.9, "factual_score": 0.85}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
