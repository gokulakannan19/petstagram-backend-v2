from fastapi import FastAPI
from app.api.v1 import auth

app = FastAPI()

app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Petstagram API Running 🚀"}