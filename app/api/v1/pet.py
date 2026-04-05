from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.services.pet import create_pet_service
from app.schemas.pet import PetCreate


router = APIRouter(prefix="/pets", tags=["Pet"])


@router.post("/")
async def create_pet(request: PetCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    create_pet_service(db=db, request=request, user_id=user.id)


@router.get("/")
async def get_pets():
    pass


@router.get("/{pet_id}")
async def get_pet_by_id():
    pass