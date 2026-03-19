class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def accelarate(self, increase):
        self.speed += increase
        return self.speed
    def brake(self, decrease):
        self.speed -= decrease
        return self.speed
    def __str__(self):
        return (f"Car : {self.brand}\n"
                f"Speed: {self.speed}km")
car_1 = Car("Toyota",200)
print(car_1)