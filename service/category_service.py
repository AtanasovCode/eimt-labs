from repository import category_repo as category

def list_all():
    return category.list_all()


def find_by_id(category_id: int):
    return category.find_by_id(category_id)