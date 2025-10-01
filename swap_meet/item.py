import uuid
from .constants import CONDITIONS

class Item:
    def __init__(self, id=None, condition=0):
        self.id = int(uuid.uuid4()) if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"

    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        return CONDITIONS.get(self.condition)       

        # match self.condition:
        #     case int(5):
        #         msg = "Excellent"
        #     case int(4):
        #         msg = "Good"
        #     case int(3):
        #         msg = "Fair"
        #     case int(2):
        #         msg = "Well used"
        #     case int(1):
        #         msg = "Poor"
        #     case int(0):
        #         msg = "Take only for yourself"
        # return msg
