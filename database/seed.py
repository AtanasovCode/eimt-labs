from sqlalchemy.orm import declarative_base
from database.database import SessionLocal
from model.models import Category, Manufacturer, Product, Base
from database.database import engine, SessionLocal


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        if db.query(Category).count() > 0:
            print("Database already seeded, skipping")
            return None
        
        categories = [
            Category(name="Electronics", description="Electronic devices"),
            Category(name="Sports", description="Sporting goods and equipment")
        ]
        
        db.add_all(categories)
        db.flush()
        
        manufacturers = [
            Manufacturer(name="Sony", address="Japan"),
            Manufacturer(name="Samsung", address="South Korea"),
            Manufacturer(name="Apple", address="USA")
        ]
        
        db.add_all(manufacturers)
        db.flush()
        
        products = [
            Product(
                name="Headphones",
                price=59.99,
                quantity=2,
                category_id=categories[0].id,
                manufacturer_id=manufacturers[0].id
            ),
            Product(
                name="Smartphone",
                price=445.95,
                quantity=6,
                category_id=categories[0].id,
                manufacturer_id=manufacturers[1].id
            )
        ]
        
        db.add_all(products)
        db.commit()
        
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()
        
        