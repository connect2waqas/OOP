"""class User:
    def __init__(self):
        self.name = "waqas"
        self.gender = "male"
    
    def login(self):
        print("Login")
        

class Student(User):
    def __init__(self):
        self.roll_no = 100

    def enroll(self):
        print("Enroll")

u = User()
s = Student()
s.login()
"""
"""class Phone:
    def __init__(self, price, brand, camera):
        self.__price = price
        self.brand = brand
        self.camera = camera
        print("Inside parent constructor.")
    @property
    def price(self):
        return self.__price
    def __show(self):
        print("private Method")
class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print("Inside child constructor.")
    
    def check(self):
        print(self.__price)
    
s = SmartPhone(2342,"iphone","15px")
s.__show()


class Phone:
    def __init__(self, price, brand, camera):
        print("Inside parent constructor.")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying a phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        # syntax for calling parent method
        super().buy()

phone = SmartPhone(4000,"Iphone","15px")
phone.buy()

class Person:
    def __init__(self, name, gender, age, profession):
        self.name = name
        self.gender = gender
        self.age = age
        self.profession = profession
        print("Inside parent constructor")

class User(Person):
    def __init__(self, name, gender, age, profession, salary):
        print("Inside child constructor")
        super().__init__(name,gender,age,profession)
        self.salary = salary
        print("inside child constructor")

doctor = User("waqas","male",23,"Doctor",5000)

We can not call super() outside the class and can only be called when we in child class unless we will get attribute error"""

# doctor.super() 
"""
class Parent:
    def __init__(self, num):
        self.__num = num
    
    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self, num, val):
        super().__init__(num)
        self.__val = val
    
    def get_val(self):
        return self.__val

son = Child(500,1000)
print(son.get_num())
print(son.get_val())"""

class Parent:
    def __init__(self):
        print("inside parent constructor.")
        self.num = 200

class Child(Parent):
    def __init__(self):
        print("inside child constructor.")
        super().__init__()
        print("inside child constructor.")
        self.val = 100
        
    
    def get_num(self):
        print(self.num)
        print(self.val)

son = Child()
son.get_num()