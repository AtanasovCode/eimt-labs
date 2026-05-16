from model.schemas import Product, ProductDto
from repository import product_repo as products
from repository import category_repo as categories, manufacturer_repo as manufacturers

def list_all():
    return products.list_all()

def find_by_id(product_id: int):
    return products.find_by_id(product_id)

def get_by_name(product_name: str):
    return products.get_by_name(product_name)

def delete_product(product_id: int):
    return products.delete_product(product_id)

def save(product_dto: ProductDto):
    category = categories.find_by_id(product_dto.category_id)
    manufacturer = manufacturers.find_by_id(product_dto.manufacturer_id)
    
    product = Product(
        id = product_dto.id,
        name = product_dto.name,
        price = product_dto.price,
        category = category,
        manufacturer = manufacturer
    )
    
    return products.save(product)

def update(product_dto: ProductDto):
    product = products.find_by_id(product_dto.id)
    product.id = product_dto.id
    product.name = product_dto.name
    product.price = product_dto.price
    product.category = categories.find_by_id(product_dto.category_id)
    product.manufacturer = manufacturers.find_by_id(product_dto.manufacturer_id)
    
    return product
