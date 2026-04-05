from fastapi import APIRouter


router = APIRouter(prefix="/pets", tags=["Pet"])


@router.post("/")
async def create_pet():
    pass


@router.get("/")
async def get_pets():
    pass


@router.get("/{pet_id}")
async def get_pet_by_id():
    pass