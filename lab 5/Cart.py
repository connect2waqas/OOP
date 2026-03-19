class cart:
    def __init__(self):
        self.items = {}
    def add_items(self,item, price):
        self.items[item] = price
        return self.items
    def remove_items(self,item):
        if item in self.items:
            del self.items[item]
            print(f"items deleted: {item}")
        else:
            print(f"items not found")
    def total_price(self):
        return sum(self.items.values())
    
add = cart()
print(add.add_items("bag", 4999))
print(add.total_price())
print(add.remove_items("bag"))