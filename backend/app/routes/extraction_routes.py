from fastapi import APIRouter,Depends
from app.schemas.email_schema import EmailInput
from app.services.ai_extractor_service import extract_deadline_from_email
from sqlalchemy.orm import Session
from app.database.models import Deadline
from app.database.dependencies import get_db

router=APIRouter(prefix="/extract",tags=["Deadline extraction"])

@router.post("/deadline")
def get_deadlines(
    db: Session = Depends(get_db)
):
    return db.query(Deadline).all()
def email_extractor(email:EmailInput,db:Session=Depends(get_db)):
    try:
        result=extract_deadline_from_email(email.subject,email.body)
        if result.get("is_relevant"):
            deadline=Deadline(
              title=result.get("title"),
              category=result.get("category"),
              event_type=result.get("event_type"),
              date=result.get("result"),
              start_time=result.get("start_time"),
              end_time=result.get("end_time"),
              action_required=result.get("action_required"),
              priority=result.get("priority"),
              confidence=result.get("confidence")  
            )
            db.add(deadline)
            db.commit()
            db.refresh(deadline)
        return result
    except Exception as e:
        return{ "error":str(e),"error type":type(e).__name__}

@router.get("/deadlines")
def get_deadlines(
    db: Session = Depends(get_db)
):
    return db.query(Deadline).all()