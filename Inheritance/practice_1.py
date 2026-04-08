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

"""
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