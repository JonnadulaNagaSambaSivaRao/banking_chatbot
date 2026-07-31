from fastapi import FastAPI

from app.routers.chatbot import router
from app.database import engine
from app import models


# Create database tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Banking AI Chatbot"
)


# Include chatbot routes
app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Banking chatbot running"
    }