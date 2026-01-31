class Person:
    def __init__(self,name , age, address):
        self.name = name
        self.age = age
        self.address = address
    def display(self):
        print(self.name)
        print(self.age)
        print(self.address)

class Student(Person):
    def __init__(self, name, age, address,roll_no,marks,):
        super().__init__(name, age, address)
        self.roll_no = roll_no
        self.marks = marks
        # self.grade = grade
    def grade(self):
        if 90 < self.marks <= 100:
            return "You got grade A"
        elif 80 < self.marks <= 90:
            return "You got grade B"
        elif 70 < self.marks <= 80:
            return "You got grade C"
        else:
            return "You got grade D"
    def display_info(self):
        grad = self.grade()
        return f"The {self.name} has got {grad}"

student1 = Student("waqas",21,"Talash",24,90)
print(student1.display_info())