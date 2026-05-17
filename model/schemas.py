from pydantic import BaseModel

class CategorySchema(BaseModel):
    id: int
    name: str
    description: str
    

class ManufacturerSchema(BaseModel):
    id: int
    name: str
    address: str

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    category: CategorySchema
    manufacturer: ManufacturerSchema


class ProductDtoSchema(BaseModel):
    id: int
    name: str
    price: float
    category_id: int
    manufacturer_id: int