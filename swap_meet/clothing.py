from .item import Item
class Clothing(Item):
    def __init__(self, id=None, condition=0, age=None, fabric="Unknown"):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):
        item_message = super().__str__()
        type_message = f"It is made from {self.fabric} fabric."
        return " ".join((item_message,type_message))
