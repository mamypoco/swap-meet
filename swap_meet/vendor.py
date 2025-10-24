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
    
    
    def get_best_by_category(self, category):

        category_items = self.get_by_category(category)

        best_condition = 0
        best_item = None

        for item in category_items:
            if item.condition > best_condition:
                best_item = item
                best_condition = item.condition

        return best_item 
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, my_best_item, their_best_item)
        
# ================Optional Enhancements================

    def get_newest_item_by_condition(self):
        """
        Return the newest item based on age, using condition as a tiebreaker.
        Items without an age value are filtered out before comparison.
        """

        valid_items = [item for item in self.inventory if item.age is not None]

        if not valid_items:
            return None
        
        best_item = valid_items[0]

        for item in valid_items:
            if item.age < best_item.age:
                best_item = item
            elif item.age == best_item.age:
                if (item.condition is not None
                    and (best_item.condition is None or item.condition > best_item.condition)):
                    best_item = item
        
        return best_item
    
    def swap_newest_items_by_condition(self, other_vendor):
        """
        Swap the newest items between vendors, using condition to break age ties.
        """

        if not self.inventory or not other_vendor.inventory:
            return False

        my_newest = self.get_newest_item_by_condition()
        their_newest = other_vendor.get_newest_item_by_condition()

        return self.swap_items(other_vendor, my_newest, their_newest)

    

