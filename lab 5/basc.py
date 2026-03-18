class Student():
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    def __str__(self):
        return (f"Student Name: {self.name}\n" 
                f"Age : {self.age}\n"
                f"Roll_no : {self.roll_no}")


student_1 = Student("Waqas",21,4022)
print(student_1)