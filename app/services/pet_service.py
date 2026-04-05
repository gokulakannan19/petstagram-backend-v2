from sqlalchemy.orm import Session
from app.repository import pet_repo
from app.schemas.pet import PetCreate


def create_pet_service(db: Session, request: PetCreate, user_id: int):
    return pet_repo.create_pet(db=db, pet_data=request.dict(), user_id=user_id)
