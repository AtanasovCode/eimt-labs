from model.schemas import Category

categories = [
    Category(id=1, name="Sport", description="Sports Category"),
    Category(id=2, name="Food", description="Food Category"),
    Category(id=3, name="Music", description="Music Category")
]

def list_all():
    return categories

def find_by_id(category_id: int):
    for c in categories:
        if c.id == category_id:
            return c
    return None