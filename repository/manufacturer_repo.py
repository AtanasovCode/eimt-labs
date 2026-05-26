from sqlalchemy.orm import Session
from model.models import Manufacturer

def list_all(db: Session):
    return db.query(Manufacturer).all()

def find_by_id(db: Session, manufacturer_id: int):
    return db.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()