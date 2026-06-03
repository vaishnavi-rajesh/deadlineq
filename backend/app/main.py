from fastapi import FastAPI
from pydantic import BaseModel
from app.services.ai_extractor_service import extract_deadline_from_email
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
def extract_test(email: EmailInput):
    try:
        result = extract_deadline_from_email(email.subject, email.body)
        return result
    except Exception as e:
        return {
            "error": str(e),
            "error_type": type(e).__name__
        }
    