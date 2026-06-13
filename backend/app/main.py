from fastapi import FastAPI
from app.routes import extraction_routes
from app.database.database import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

app= FastAPI (
    title="DeadlineQ API",
    description="AI powered Gmail assistant",
    version="0.1.0"
)

app.include_router(extraction_routes.router)

@app.get("/")
def root():
    return{
        "message":"DeadlineQ running successfully",
        "status":"ok"
    }
    