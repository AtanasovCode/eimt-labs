from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.schemas import ProductSchema, ProductDtoSchema
from service import product_service as products


router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("/", response_model=list[ProductSchema])
async def list_all():
    return products.list_all()

@router.get("/{product_id}", response_model=ProductSchema)
async def find_by_id(product_id: int):
    product = products.find_by_id(product_id)
    
    if product is not None:
        return product
    
    return JSONResponse(status_code=404, content={"message": f"Product with id {product_id} not found"})


@router.get("/search/{product_name}", response_model=list[ProductSchema])
async def get_product_by_name(product_name: str):
    products_with_target_name = products.get_by_name(product_name)
    
    if products_with_target_name is not None and len(products_with_target_name) > 0:
        return products_with_target_name
    return JSONResponse(status_code=404, content={"message": f"No results found!"})


@router.post("/", response_model=ProductSchema)
async def create_product(product_dto: ProductDtoSchema):
    return products.save(product_dto)


@router.put("/", response_model=ProductSchema)
async def update_product(product_dto: ProductDtoSchema):
    product = products.find_by_id(product_dto.id)
    
    if product is not None:
        return products.update(product_dto)

    return JSONResponse(status_code=404, content={"message": "Product not found"})

@router.delete("/")
async def delete_product(product_dto: ProductDtoSchema):
    product = products.find_by_id(product_dto.id)
    
    if product is not None:
        products.delete_product(product_dto.id)
        return JSONResponse(status_code=200, content={"message": f"Product with id {product_dto.id} deleted"})
    
    return JSONResponse(status_code=404, content={"message": "Product not found"})