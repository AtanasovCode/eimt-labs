from sqlalchemy.orm import Session
from repository import product_repo as products
from model.schemas import (
    ProductCreate,
    ProductUpdate,
)

def list_all(db: Session):
    return products.list_all(db)

def find_by_id(db: Session, product_id: int):
    return products.find_by_id(db, product_id)

def get_by_name(db: Session, product_name: str):
    return products.get_by_name(db, product_name)

def delete(db: Session, product_id: int):
    return products.delete(db, product_id)

def save(db: Session, product_create: ProductCreate):
    return products.save(db, product_create)

def update(db: Session, product_update: ProductUpdate, product_id: int):
    return products.update(db, product_update, product_id)