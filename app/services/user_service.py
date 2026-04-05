from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repository.user_repo import get_user_by_email, create_user
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = pwd_context.hash(password)
    return create_user(db, email, hashed_password)

