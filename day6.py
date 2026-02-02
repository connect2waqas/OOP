class Vector1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other,Vector):
            return Vector1(self.x + other.x , self.y + other.y)
        raise TypeError("Can only add vector to vector")
    def __sub__(self, other):
        if isinstance(other,Vector):
            return Vector1(self.x - other.x , self.y - other.y)
        raise TypeError("Can only substract vector from vector")
    def __mul__(self, scalar):
        if isinstance(scalar,(int,float)):
            return Vector1(self.x * scalar, self.y * scalar)
        raise TypeError("Can only multiply vector by vector")
    def __truediv__(self, scalar):
        if isinstance(scalar,(int,float)):
            if scalar == 0:
                raise ValueError("Cannot be divid by Zero")
            return Vector1(self.x / scalar, self.y / scalar)
        raise TypeError("Can only divide vector by number")
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector1(3,4)
v2 = Vector1(2,1)
print("Addition:", v1 + v2)
print("Substraction:", v1 - v2)
print("Multiplication:", v1 * 3)
print("Division:", v1 / 2)
print("Division:",v2 / 2)
