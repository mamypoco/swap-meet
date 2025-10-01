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
    
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, their_first_item)
    
    def get_by_category(self, category):
        
        return [item for item in self.inventory if item.get_category() == category]
    
    def get_best_by_category(self, category): #category = "Clothing"
        self.inventory
        category_items = self.get_by_category(category) # ["Clothing1, 5", "Clothing2, 2"]

        if not category_items:
            return None

        # pick the best item and the instance of the best item
    
    def swap_best_by_category(self, other_vender, my_priority, their_priority):
        pass

