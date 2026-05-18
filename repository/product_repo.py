from sqlalchemy.orm import Session

from model.models import Product
from model.schemas import (
ProductSchema,
ProductCreate,
ProductUpdate,
)

def list_all(db: Session):
    return db.query(Product).all()

def find_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_by_name(db: Session, product_name: str):
    return db.query(Product).filter(Product.name == product_name).all()


def save(db: Session, product_create: ProductCreate):
    new_product = Product(
        name = product_create.name,
        price = product_create.price,
        quantity = product_create.quantity,
        category_id = product_create.category_id,
        manufacturer_id = product_create.manufacturer_id
    )
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
    
    
def update(db: Session, product_update: ProductUpdate, product_id: int):
    product = find_by_id(db, product_id)
    
    if not product:
        return None
    
    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
        
    db.commit()
    db.refresh(product)
    return product


def delete(db: Session, product_id: int):
    product = find_by_id(db, product_id)
    if product:
        db.delete(product)
        db.commit()
    return product