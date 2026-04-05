from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session
from app.models.pet import Pet


def create_pet(db: Session, pet_data: dict, user_id: int):
    pet = Pet(**pet_data, owner_id=user_id)
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet


def get_pets_by_user(db: Session, user_id: int):
    pets = db.query(Pet).filter(Pet.owner_id == user_id).all()
    if not pets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No pets found for this user")
    return pets
