from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI (
    title="DeadlineQ API",
    description="AI powered Gmail assistant",
    version="0.1.0"
)

class EmailInput(BaseModel):
    subject:str
    body:str

@app.get("/")
def root():
    return{
        "message":"DeadlineQ running successfully",
        "status":"ok"
    }

@app.post("/extract-test")
def extract_test(email:EmailInput):
    return{
        "received subject":email.subject,
        "received body":email.body,
        "message":"email received successfully"
    }