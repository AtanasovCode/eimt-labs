from sqlalchemy.orm import Session
from repository import category_repo as categories

def list_all(db: Session):
    return categories.list_all(db)


def find_by_id(db: Session, category_id: int):
    return categories.find_by_id(db, category_id)