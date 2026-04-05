from fastapi import APIRouter, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db, get_current_user
from app.repository.pet_repo import get_pets_by_user
from app.services.pet_service import create_pet_service
from app.schemas.pet import PetCreate, PetOut


router = APIRouter(prefix="/pets", tags=["Pet"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PetOut)
async def create_pet(request: PetCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return create_pet_service(db=db, request=request, user_id=user.id)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[PetOut])
async def get_pets(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_pets_by_user(db=db, user_id = user.id)


@router.get("/{pet_id}")
async def get_pet_by_id():
    pass