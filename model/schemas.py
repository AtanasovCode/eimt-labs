from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str
    description: str
    

class Manufacturer:
    id: int
    name: str
    address: str

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: Category
    manufacturer: Manufacturer


class ProductDto(BaseModel):
    id: int
    name: str
    price: float
    category_id: int
    manufacturer_id: int