from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserCreate
from app.services.user_service import register_user


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user.email, user.password)
