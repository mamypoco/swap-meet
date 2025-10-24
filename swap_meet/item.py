from uuid import uuid4
from .constants import CONDITIONS
from.errors import InvalidIDError
from math import floor
class Item:

    """
    NOTE:
    Raises: InvalidIDError: If the provided ID is not an integer.
    """

    def __init__(self, id=None, condition=0, age=None):
        self.id = uuid4().int if id is None else id

        if not isinstance(self.id, int):
            raise InvalidIDError(self.id)
        
        self.condition = condition
        self.age = age

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        # If we are not allowed to use floor, I'll use int((self.condition + 0.5) // 1).
        # The only downside is that for negative numbers, it rounds down (e.g., -2.4 becomes -3).
        # Chose not to use .round because it has unexpected behavior ex 2.5 -> 2
        condition = floor(self.condition + 0.5)
        msg = CONDITIONS[condition]
        return msg