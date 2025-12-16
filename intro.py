class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print("Welcome!")

    def inner(self):
        print("We are calling the staticmethod")
        print(self.hello())
s1= Student("waqas",87)
print(s1.inner())
# print(s1.name,s1.marks)

class Car():
    # constructor function or constructor Method
    def __init__(self,name, car_name):
        self.brand_name = name
        self.car_name = car_name
    
    def getName(self):
        return f"{self.brand_name},\n {self.car_name}"

car1 = Car("toyata","civic")
car2 = Car("BMW","HOnda")

print(car1.getName())