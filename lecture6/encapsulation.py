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