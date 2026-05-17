from repository import category_repo as categories

def list_all():
    return categories.list_all()


def find_by_id(category_id: int):
    return categories.find_by_id(category_id)