from pydantic import BaseModel
from typing import Optional


class PetCreate(BaseModel):
    name: str
    breed: Optional[str]
    age: Optional[int]
    photo_url: Optional[str]


class PetOut(BaseModel):
    id: int
    name: str
    breed: Optional[str]
    age: Optional[int]
    photo_url: Optional[str]

    class Config:
        from_attributes = True
