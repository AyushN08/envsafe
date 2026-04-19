from fastapi import FastAPI
from app.api.routes import webhook

app = FastAPI()

app.include_router(webhook.router)

@app.get("/")
def root():
    return {"message": "EnvSafe is running"} 