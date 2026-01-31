class Person:
    person_details = {}
    def __init__(self,name , age, address):
        self.name = name
        self.age = age
        self.address = address
    def display(self):
        ls = [self.name,self.age,self.address]
        return ls
class Student(Person):
    def __init__(self, name, age, address,roll_no,marks,):
        super().__init__(name, age, address)
        self.roll_no = roll_no
        self.marks = marks
        # self.grade = grade
    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            return "A"
        elif 80 < self.marks <= 90:
            return "B"
        elif 70 < self.marks <= 80:
            return "C"
        else:
            return "D"
    def display_info(self):
        grad = self.calculate_grade()
        return f"Name: {self.name}, Roll no: {self.roll_no}, Grade: {grad}"
class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary
    def give_assignment(self):
        print("this is your assignments")

    def display(self):
        employee_info = super().display()[:2] + [self.address, self.subject, self.salary]
        Person.person_details[self.employee_id] = employee_info
        return employee_info
    
    
    
student1 = Student("waqas",21,"Talash",24,90)
teacher1 = Teacher("Ilyas",19,"Talash",3234,"Electronic Engineer",90000)
print(student1.display_info())
print(teacher1.display())
print(Person.person_details)