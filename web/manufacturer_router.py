from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from service import manufacturer_service as manufacturers
from model.schemas import ManufacturerSchema


router = APIRouter(prefix="/api/manufacturers", tags=["manufacturers"])

@router.get("/", response_model=list[ManufacturerSchema])
async def get_all(db: Session = Depends(get_db)):
    return manufacturers.list_all(db)
