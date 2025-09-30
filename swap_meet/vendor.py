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
        # ids = []
        # for item in inventory:
        #     ids.append(item.id)
        # return ids
    
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
    
        # for index in range(len(their_ids)):
        #     current_id = their_ids[index]
        #     if current_id == their_id:
        #         self.inventory.append(other_vendor.inventory[index])
        #         other_vendor.inventory[index] = other_vendor.inventory[-1]
        #         other_vendor.inventory.pop()

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first = self.inventory[0]
        their_first = other_vendor.inventory[0]

        other_vendor.inventory.append(my_first)
        self.inventory.append(their_first)

        self.inventory[0] = self.inventory[-1]
        self.inventory.pop()

        other_vendor.inventory[0] = other_vendor.inventory[-1]
        other_vendor.inventory.pop()
    
        return True
    

