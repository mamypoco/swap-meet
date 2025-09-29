class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        
        for index in range(len(self.inventory)):
            current_item = self.inventory[index]
            if current_item == item:
                self.inventory[index] = self.inventory[-1] 
                self.inventory.pop()
                break
    
        return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
            
        return None


