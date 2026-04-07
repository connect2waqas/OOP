"""Pass by Reference"""

class Person:

    def __init__(self, name, age,):
        self.name = name
        self.age = age
    
# def greet(person):
#     print(f"I am {person.name} and i am {person.age} year old")
#     p1 = Person("ilyas", 19)
#     return p1
# p = Person("Waqas",22)
# q = p
# # greet(p)
# # greet(q)
# x = greet(p)
# print(x)
# print(x.name)
# print(x.age)

def greet(person):
    person.name = "ilyas"
    return person

p = Person("waqas",23)
print(id(p))
x = greet(p)
print(id(x))

class Atm:
    
    def __init__(self, pin, balance):
        self.pin = pin
        self.__balance = balance
    
    def get_balance(self):
        pin = int(input("Enter pin: "))
        if pin == self.pin:
            print(self.__balance)
        else:
            print("Wrong pin")
    def deposit(self, amount):
        pin = int(input("Enter pin: "))
        if self.change_pin(pin) and amount > 0:
            self.__balance += amount
        else:
            print("Wrong pin or amount")
    def check_pin(self,pin):
        return True if pin == self.pin else False
    def change_pin(self):
        pin = int(input("Enter pin:"))
        if self.check_pin(pin):
            self.pin = pin
        else:
            print("Wrong pin")

b = Atm(1234,9000)
