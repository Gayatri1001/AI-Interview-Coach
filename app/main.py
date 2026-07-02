from fastapi import FastAPI

app = FastAPI(
    title="AI Interview Coach API",
    version="1.0.0",
    description="Backend API for AI Interview Coach"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Coach API"
    }