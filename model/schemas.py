from pydantic import BaseModel
from typing import Optional

class CategorySchema(BaseModel):
    id: int
    name: str
    description: str
    
    class Config:
        from_attributes = True
    
    
class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    category_id: int
    manufacturer_id: int
    
    
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category_id: Optional[int] = None
    manufacturer_id: Optional[int] = None
    
    

class ManufacturerSchema(BaseModel):
    id: int
    name: str
    address: str
    
    class Config:
        from_attributes = True
        

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    category: CategorySchema
    manufacturer: ManufacturerSchema
    
    class Config:
        from_attributes = True


class ProductDtoSchema(BaseModel):
    id: int
    name: str
    price: float
    category_id: int
    manufacturer_id: int
    
    class Config:
        from_attributes = True