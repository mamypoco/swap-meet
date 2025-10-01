from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        item_message = super().__str__()
        type_message = f"This is a {self.type} device."
        return " ".join((item_message,type_message))