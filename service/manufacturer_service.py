from repository import manufacturer_repo as manufacturers

def list_all():
    return manufacturers.list_all()


def find_by_id(manufacturer_id: int):
    return manufacturers.find_by_id(manufacturer_id)