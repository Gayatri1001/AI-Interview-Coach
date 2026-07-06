from fastapi import FastAPI
from app.routers import home


app = FastAPI(
    title="AI Interview Coach API",
    version="1.0.0",
)

app.include_router(home.router)

