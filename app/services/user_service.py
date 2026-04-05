from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repository.user_repo import get_user_by_email, create_user
from app.core.security import hash_password


def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(password)
    return create_user(db, email, hashed_password)

