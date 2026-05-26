from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from database.database import get_db
from fastapi.responses import JSONResponse
from model.schemas import ProductSchema, ProductCreate, ProductUpdate, CategorySchema
from service import product_service as products, category_service as categories


router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("/", response_model=list[ProductSchema])
async def list_all(db: Session = Depends(get_db)):
    return products.list_all(db)


@router.get("/categories", response_model=list[CategorySchema])
async def list_categories(db: Session = Depends(get_db)):
    return categories.list_all(db)

@router.get("/{product_id}", response_model=ProductSchema)
async def find_by_id(product_id: int, db: Session = Depends(get_db)):
    product = products.find_by_id(db, product_id)
    
    if product is not None:
        return product
    
    return JSONResponse(status_code=404, content={"message": f"Product with id {product_id} not found"})


@router.get("/search/{product_name}", response_model=list[ProductSchema])
async def get_product_by_name(product_name: str, db: Session = Depends(get_db)):
    products_with_target_name = products.get_by_name(db, product_name)
    
    if products_with_target_name is not None and len(products_with_target_name) > 0:
        return products_with_target_name
    return JSONResponse(status_code=404, content={"message": f"No results found!"})


@router.post("/", response_model=ProductSchema)
async def create(product_create: ProductCreate, db: Session = Depends(get_db)):
    return products.save(db, product_create)


@router.put("/", response_model=ProductSchema)
async def update(product_update: ProductUpdate, product_id: int, db: Session = Depends(get_db)):
    product = products.find_by_id(db, product_id)
    
    if product is not None:
        return products.update(db, product_update, product_id)

    return JSONResponse(status_code=404, content={"message": "Product not found"})

@router.delete("/")
async def delete(product_id: int, db: Session = Depends(get_db)):
    product = products.find_by_id(db, product_id)
    
    if product is not None:
        products.delete(db, product_id)
        return JSONResponse(status_code=200, content={"message": f"Product with id {product_id} deleted"})
    
    return JSONResponse(status_code=404, content={"message": "Product not found"})