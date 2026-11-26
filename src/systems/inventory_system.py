class InventorySystem:
    def __init__(self, registry):
        self.registry = registry
        self.items = {}

    def add_item(self, item_id, qty=1):
        if item_id in self.registry:
            self.items[item_id] = self.items.get(item_id, 0) + qty

    def remove_item(self, item_id, qty=1):
        if self.items.get(item_id, 0) >= qty:
            self.items[item_id] -= qty
            if self.items[item_id] == 0:
                del self.items[item_id]
            return True
        return False
