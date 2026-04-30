class Product:
    def discount(self):
        return f"Discount for products == 5"

class Book(Product):
    def discount(self):
        return f"Discount for books == 10"
    
class Laptop(Product):
    def discount(self):
        return f"Discount for laptop == 20"
class Phone(Product):
    def discount(self):
        return f"Discount for phones == 30"

print("1st method:")
categories = [Product(), Book(), Laptop(), Phone()]
for categery in categories:
    print(categery.discount())

print()
print()
print("2nd Method:")
def categray_call(obj):
    print(obj.discount())

for i in categories:
    categray_call(i)