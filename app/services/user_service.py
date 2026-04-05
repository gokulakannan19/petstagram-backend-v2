from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repository.user_repo import get_user_by_email, create_user
from app.core.security import create_access_token, hash_password, verify_password


def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(password)
    return create_user(db, email, hashed_password)


def login_user(db, email, password):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = create_access_token({"sub": str(user.id)})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
