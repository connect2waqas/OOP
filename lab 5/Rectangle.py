class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def  Area_of_rectangle(self):
        self.area = self.length * self.width
        return self.area
    def perimeter_of_rectangle(self):
        self.perimeter = 2 * (self.length + self.width)
        return self.perimeter
rectangle_1 = Rectangle(5,6)
Rectangle_2 = Rectangle(9,8)

print(f"Area of rectangle: {rectangle_1.Area_of_rectangle()}")
print(f"Perimeter of Rectangle: {Rectangle_2.perimeter_of_rectangle()}")