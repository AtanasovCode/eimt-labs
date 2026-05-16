from model.schemas import Manufacturer

manufacturers = [
    Manufacturer(id=1, name="Nike", address="USA"),
    Manufacturer(id=2, name="KFC", address="USA"),
    Manufacturer(id=3, name="A Records", address="UK")
]

def list_all():
    return manufacturers

def find_by_id(manufacturer_id: int):
    for m in manufacturers:
        if m.id == manufacturer_id:
            return m
    return None