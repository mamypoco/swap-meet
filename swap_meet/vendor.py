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

    def _get_inventory_ids(self, inventory):
        """Return a list of item IDs from the given inventory."""
        return [item.id for item in inventory]

    def _transfer_item_by_id(self, item_id, item_ids, vendor):
        """
        Move the item with item_id from self.inventory to other_vendor.inventory.
        Returns True if moved, False if not found.
        NOTE: Removal uses 'replace-with-last + pop', which changes order.
        """
        for index in range(len(item_ids)):
            current_id = item_ids[index]
            if current_id == item_id:
                vendor.inventory.append(self.inventory[index])
                self.inventory[index] = self.inventory[-1]
                self.inventory.pop()
                break

    def swap_items(self, other_vendor, my_item, their_item):

        if not self.inventory or not other_vendor.inventory:
            return False

        my_ids = self._get_inventory_ids(self.inventory)
        their_ids = other_vendor._get_inventory_ids(other_vendor.inventory)

        my_id = my_item.id
        their_id = their_item.id

        if my_id not in my_ids or their_id not in their_ids:
            return False

        self._transfer_item_by_id(my_id, my_ids, other_vendor)
        other_vendor._transfer_item_by_id(their_id, their_ids, self)

        return True

    def swap_first_item(self, other_vendor):
        
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, their_first_item)

    def get_by_category(self, category):
        
        result = []

        for item in self.inventory:
            item_category = item.get_category()
            if item_category == category:
                result.append(item)

        return result

    def get_best_by_category(self, category):
        
        category_items = self.get_by_category(category)

        if not category_items:
            return None
        
        best_item = category_items[0]
        best_condition = category_items[0].condition
        
        for item in category_items:
            if item.condition > best_condition:
                best_item = item
                best_condition = item.condition

        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False

        self.swap_items(other_vendor, my_best_item, their_best_item)

        return True