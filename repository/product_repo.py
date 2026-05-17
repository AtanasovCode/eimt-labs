from model.schemas import ProductSchema
from repository import category_repo as category, manufacturer_repo as manufacturer

products = [
    ProductSchema(id=1, name="Shirt", price=14.99,
            category=category.find_by_id(1),
            manufacturer=manufacturer.find_by_id(1)
            ),
    ProductSchema(id=2, name="Bucket", price=12.25,
            category=category.find_by_id(2),
            manufacturer=manufacturer.find_by_id(2))
]

def list_all():
    return products

def find_by_id(product_id: int):
    for p in products:
        if p.id == product_id:
            return p
    return None

def get_by_name(product_name: str):
    products_with_target_name = []
    for p in products:
        if p.name == product_name:
            products_with_target_name.append(p)
    return products_with_target_name


def save(product: ProductSchema):
    products.append(product)
    return product

def delete_product(product_id: int):
    for p in products:
        if p.id == product_id:
            products.remove(p)
            