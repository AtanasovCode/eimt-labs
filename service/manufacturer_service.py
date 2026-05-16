from repository import manufacturer_repo as manufacturer

def list_all():
    return manufacturer.list_all()


def find_by_id(manufacturer_id: int):
    return manufacturer.find_by_id(manufacturer_id)