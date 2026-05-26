from sqlalchemy.orm import Session
from repository import manufacturer_repo as manufacturers

def list_all(db: Session):
    return manufacturers.list_all(db)


def find_by_id(db: Session, manufacturer_id: int):
    return manufacturers.find_by_id(db, manufacturer_id)