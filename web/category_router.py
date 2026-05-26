from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from service import category_service as categories
from model.schemas import CategorySchema


router = APIRouter(prefix="/api/categories", tags=["Category"])


@router.get("/", response_model=list[CategorySchema])
async def get_categories(db: Session = Depends(get_db)):
    return categories.list_all(db)

@router.get("/{category_id}", response_model=CategorySchema)
async def get_by_id(category_id: int, db: Session = Depends(get_db)):
    return categories.find_by_id(db, category_id)