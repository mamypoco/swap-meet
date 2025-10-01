from uuid import uuid4
from .constants import CONDITIONS
class Item:
    def __init__(self, id=None, condition=0):
        self.id = int(uuid4()) if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        msg = CONDITIONS[self.condition]
        return msg

