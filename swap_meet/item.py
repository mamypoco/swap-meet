import uuid
class Item:
    def __init__(self, id=None):
        unique_id = int(uuid.uuid4())
        print(unique_id)
        self.id = unique_id if id is None else id 

    def get_category(self):
        return "Item"
    
    


