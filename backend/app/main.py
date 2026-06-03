from fastapi import FastAPI

app= FastAPI (
    title="DeadlineQ API",
    description="AI powered Gmail assistant",
    version="0.1.0"
)

@app.get("/")
def root():
    return{
        "message":"DeadlineQ running successfully",
        "status":"ok"
    }