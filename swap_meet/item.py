from uuid import uuid4
from .constants import CONDITIONS
from.errors import InvalidIDError
class Item:
    """
    NOTE:
    Raises: InvalidIDError: If the provided ID is not an integer.
    """

    def __init__(self, id=None, condition=0, age=None):
        self.id = int(uuid4()) if id is None else id

        if not isinstance(self.id, int):
            raise InvalidIDError(self.id)
        
        self.condition = condition
        self.age = age

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        msg = CONDITIONS.get(self.condition)
        return msg
    

