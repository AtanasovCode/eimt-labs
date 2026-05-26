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
    category_id = Column(Integer, ForeignKey("categories.id"))
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    
    category = relationship("Category", back_populates="products")
    manufacturer = relationship("Manufacturer", back_populates="products")



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    cart = relationship("Cart", back_populates="user")



class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="cart")
    items = relationship("CartItem", back_populates="cart")


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")