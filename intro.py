class CMS():
    University_name = "UOH"
    def __init__(self,name, reg_no, semester):
        self.name = name
        self.reg_no = reg_no
        self.semester = semester

    
    def get_Enroll(self):
        return f"""
        Student Name: {self.name}
        Student Roll No : {self.reg_no}
        Student semester: {self.semester}"""

    
    def upgrade_semester(self,new_semester):
        self.semester = new_semester
        return f"Your are promoted to semester: {self.semester}"
    @classmethod
    def welcome(cls):
        return f"Welcome to {CMS.University_name}"
    

name = input("Enter name: ")
reg_no = int(input("Enter Roll No: "))
semester = int(input("Enter semseter NO: "))
student_1 = CMS(name,reg_no,semester,)
print(student_1.welcome())
print(student_1.get_Enroll())
new_semester = input("Enter semester: ")
print(student_1.upgrade_semester(new_semester))

