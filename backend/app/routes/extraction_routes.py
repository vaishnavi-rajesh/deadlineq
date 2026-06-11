from fastapi import APIRouter
from app.schemas.email_schema import EmailInput
from app.services.ai_extractor_service import extract_deadline_from_email

router=APIRouter(prefix="/extract",tags=["Deadline extraction"])

@router.post("/deadline")
def email_extractor(email:EmailInput):
    try:
        result=extract_deadline_from_email(email.subject,email.body)
        return result
    except Exception as e:
        return{ "error":str(e),"error type":type(e).__name__}
