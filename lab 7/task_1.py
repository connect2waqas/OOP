class Dog:
    def sound(self):
        print("woop")

class Cat:
    def sound(self):
        print("meow")

class Bird:
    def sound(self):
        print("chires")


dog, cat , bird = Dog(), Cat(), Bird()

animals = [dog,cat,bird]
for animal in animals:
    animal.sound()