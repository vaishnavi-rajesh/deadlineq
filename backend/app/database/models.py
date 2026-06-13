from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Date,Integer,String,Boolean

class Base(DeclarativeBase):
    pass
class Deadline(Base):
    __tablename__="deadline"
    id=Column(Integer,primary_key=True,index=True)
    is_relevant=Column(Boolean)
    title=Column(String)
    category=Column(String)
    event_type=Column(String)
    date=Column(String)
    start_time=Column(String)
    end_time=Column(String)
    action_required=Column(String)
    priority=Column(String)
    confidence=Column(Boolean)