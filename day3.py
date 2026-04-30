"""
Polymorphism means "many forms" - it allows us to use the same interface for different data types.
"""

# ==========================================
# 1. BASIC POLYMORPHISM WITH FUNCTIONS
# ==========================================

def add(a, b, c=0):
    """Same function name, different number of parameters"""
    return a + b + c

print("Function Polymorphism:")
print(f"add(2, 3) = {add(2, 3)}")
print(f"add(2, 3, 4) = {add(2, 3, 4)}")
print()

# Built-in polymorphic function
print("Built-in len() works with different types:")
print(f"len('Hello') = {len('Hello')}")
print(f"len([1, 2, 3]) = {len([1, 2, 3])}")
print(f"len({{'a': 1, 'b': 2}}) = {len({'a': 1, 'b': 2})}")
print()

# ==========================================
# 2. POLYMORPHISM WITH CLASS METHODS
# ==========================================

class Dog:
    def speak(self):
        return "Woof! Woof!"
    
    def move(self):
        return "Dog runs on four legs"

class Cat:
    def speak(self):
        return "Meow! Meow!"
    
    def move(self):
        return "Cat walks gracefully"

class Bird:
    def speak(self):
        return "Chirp! Chirp!"
    
    def move(self):
        return "Bird flies in the sky"

# Polymorphism in action
print("Polymorphism with different classes:")
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")
    print(f"  {animal.move()}")
print()

# ==========================================
# 3. POLYMORPHISM WITH INHERITANCE
# ==========================================

class Shape:
    """Parent class"""
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

print("Polymorphism with Inheritance:")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 5, 5, 6)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Area: {shape.area()}")
    print(f"  Perimeter: {shape.perimeter()}")
print()

# ==========================================
# 4. METHOD OVERRIDING
# ==========================================

class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"I am {self.name}"

class Lion(Animal):
    def sound(self):  # Overriding parent method
        return "Roar!"

class Cow(Animal):
    def sound(self):  # Overriding parent method
        return "Moo!"

print("Method Overriding:")
animals = [Lion("Simba"), Cow("Bessie")]
for animal in animals:
    print(f"{animal.info()} and I say: {animal.sound()}")
print()

# ==========================================
# 5. OPERATOR OVERLOADING (Special Methods)
# ==========================================

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        """Overload str() function"""
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

print("Operator Overloading:")
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Using overloaded + operator
print(f"{p1} + {p2} = {p3}")
print(f"p1 == p2: {p1 == p2}")
print()

# ==========================================
# 6. DUCK TYPING
# ==========================================
# "If it walks like a duck and quacks like a duck, it's a duck"

class Duck:
    def swim(self):
        return "Duck is swimming"

class Fish:
    def swim(self):
        return "Fish is swimming"

class Airplane:
    def fly(self):
        return "Airplane is flying"

def make_it_swim(creature):
    """Duck typing - we don't check the type, just if it has swim() method"""
    print(creature.swim())

print("Duck Typing:")
make_it_swim(Duck())
make_it_swim(Fish())
# make_it_swim(Airplane())  # This would cause an error
print()

# ==========================================
# 7. PRACTICAL EXAMPLE - Payment System
# ==========================================

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement this method")

class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card"

class PayPal(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"

class Bitcoin(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin"

def process_payment(payment_method, amount):
    """Process payment regardless of payment type"""
    print(payment_method.pay(amount))

print("Real-world Polymorphism Example:")
payments = [CreditCard(), PayPal(), Bitcoin()]
for payment in payments:
    process_payment(payment, 100)
print()

print("This was polymorpism")
