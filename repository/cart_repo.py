from sqlalchemy.orm import Session
from model.models import Cart, CartItem, Product
from model.schemas import CartItemCreate

def get_cart_by_user(db: Session, user_id: int):
    return db.query(Cart).filter(Cart.user_id == user_id).first()

def get_cart_items(db: Session, cart_id: int):
    return db.query(CartItem).filter(CartItem.cart_id == cart_id).all()

def create_cart(db: Session, user_id: int):
    new_cart = Cart(user_id = user_id)

    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)

    return new_cart



def add_item_to_cart(db: Session, cart_id: int, item_data: CartItemCreate):
    new_item = CartItem(
        cart_id = cart_id,
        **item_data.model_dump()
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


def remove_item_from_cart(db: Session, cart_id: int, item_id: int):
    item = db.query(CartItem).filter(
        CartItem.cart_id == cart_id,
        CartItem.id == item_id
    ).first()

    if not item:
        return None

    db.delete(item)
    db.commit()
    return item



def clear_cart(db: Session, cart_id: int):
    db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()
    db.commit()


def buy_items(db: Session, cart_id: int):
    cart_items = get_cart_items(db, cart_id)

    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product or product.quantity > item.quantity:
            raise ValueError(f"Insufficient stock for product {item.product_id}")
        product.quantity -= item.quantity

    db.query(CartItem).filter(CartItem.cart_id == cart_id).delete()
    db.commit()