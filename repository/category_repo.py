from sqlalchemy.orm import Session
from model.models import Category

def list_all(db: Session):
    return db.query(Category).all()

def find_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()