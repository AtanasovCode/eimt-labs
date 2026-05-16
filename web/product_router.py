from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.schemas import Product
from service import product_service as products


router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("/", response_model=list[Product])
async def list_all():
    return products.list_all()

@router.get("/{product_id}", response_model=Product)
async def find_by_id(product_id: int):
    product = products.find_by_id(product_id)
    
    if product is not None:
        return product
    
    return JSONResponse(status_code=404, content={"message": f"Product with id {product_id} not found"})
