from fastapi import APIRouter
from model.schemas import Product
from service import product_service as products


router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("/", response_model=list[Product])
async def list_all():
    return products.list_all()