def grade(student,marks):
    if len(student) != len(marks):
        return
    for name, mark in zip(student,marks):
        if mark >= 90:
            grade = "A"
        elif 80 <= mark < 90:
            grade = "B"
        elif 70 <= mark < 80:
            grade = "C"
        else:
            grade = "F"
        print(f"{name} has grade: {grade}")
student = ["waqas","Abbas","bashir","ilyas"]
marks = [67,95,48,37]
grade(student,marks)