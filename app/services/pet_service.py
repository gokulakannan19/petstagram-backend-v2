from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.repository import pet_repo
from app.schemas.pet import PetCreate


def create_pet_service(db: Session, request: PetCreate, user_id: int):
    return pet_repo.create_pet(db=db, pet_data=request.dict(), user_id=user_id)


def get_user_pets_service(db: Session, user_id: int):
    pets = pet_repo.get_pets_by_user(db, user_id)
    if not pets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No pets found for this user")
    return pets


def get_pet_service(db: Session, pet_id: int, user_id: int):
    pet = pet_repo.get_pet_by_id(db, pet_id)

    if not pet or pet.owner_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet not found")

    return pet