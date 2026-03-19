class Product:
    def __init__(self , name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.products = []
    def add_products(self, product):
        self.products.append(product)
        print(f"{product.name} added to order")
    def calculate_total(self):
        total = 0
        for p in self.products:
            total += p.price
        print("total prices = ", total)


p1 = Product("shoes",2000)
p2 = Product("shirt",1500)
p3 = Product("watch", 3000)

o = Order()
o.add_products(p1)
o.add_products(p2)
o.add_products(p3)
o.calculate_total()