from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.schemas import Product, ProductDto
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


@router.get("/search/{product_name}", response_model=list[Product])
async def get_product_by_name(product_name: str):
    products_with_target_name = products.get_by_name(product_name)
    
    if products_with_target_name is not None and len(products_with_target_name) > 0:
        return products_with_target_name
    return JSONResponse(status_code=404, content={"message": f"No results found!"})


@router.post("/", response_model=Product)
async def create_product(product_dto: ProductDto):
    return products.save(product_dto)


@router.put("/", response_model=Product)
async def update_product(product_dto: ProductDto):
    product = products.find_by_id(product_dto.id)
    
    if product is not None:
        return products.update(product_dto)

    return JSONResponse(status_code=404, content={"message": "Product not found"})