from model.schemas import Product
from repository import category_repo as category
from repository import manufacturer_repo as manufacturer

products = [
    Product(id=1, name="Shirt", price=14.99,
            category=category.find_by_id(1),
            manufacturer=manufacturer.find_by_id(1)
            ),
    Product(id=2, name="Bucket", price=12.25,
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


def save(product: Product):
    products.append(product)
    return product

def delete_product(product_id: int):
    for p in products:
        if p.id == product_id:
            products.remove(p)
            