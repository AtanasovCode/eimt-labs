from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    
    products = relationship("Product", back_populates="category")
    
    
class Manufacturer(Base):
    __tablename__ = "manufacturers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    
    products = relationship("Product", back_populates="manufacturer")
    

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey="categories.id")
    manufacturer_id = Column(Integer, ForeignKey="manufacturers.id")
    
    category = relationship("Category", back_populates="products")
    manufacturer = relationship("Manufacturer", back_populates="products")