from .item import Item

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


    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        
        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        my_first_item = self.inventory[0]
        friend_first_item = other_vendor.inventory[0]
        
        this_item_removed = self.remove(my_first_item)
        other_vendor.add(this_item_removed)
        
        friend_item_removed = other_vendor.remove(friend_first_item)
        self.add(friend_item_removed)

        return True




