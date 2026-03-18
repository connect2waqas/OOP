class Result_Mangnment_system:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def add_marks(self, marks):
        self.marks = marks
    
    def student_marks(self):
        total_mark = sum(self.marks)
        return total_mark
    def average_marks(self):
        avg_marks = sum(self.marks) / len(self.marks)
        return avg_marks
    def get_grade(self):
        # self.avg= self.average_marks()
        if self.average_marks() >= 80:
            grade = "A"
        elif 80 < self.average_marks() >= 60:
            grade = "B"
        elif self.avg >= 50:
            grade = "C"
        else:
            grade = "F"
        return grade
    def __str__(self):
        return (
            f"Name : {self.name}\n" 
            f"Roll No: {self.roll_number}\n"
            f"Total marks: {self.marks}\n"
            f"Student Total: {self.student_marks()}\n"
            f"Grade: {self.get_grade()}\n"
            f"Average: {self.average_marks():.2f}"
        )
    def is_passed(self):
        return "Pass" if self.get_grade() != "F" else "Fail"


student_1 = Result_Mangnment_system("waqas Ahmad", 1020)
student_1_marks = [90,89,90]
student_1.add_marks(student_1_marks)
print(student_1)
print("==================================== Task 2 =====================================")
student_2 = Result_Mangnment_system("Ilyas khan",2300)
student_2_marks = [87,89,32]
student_2.add_marks(student_1_marks)
print(student_2.is_passed())

