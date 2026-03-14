def student_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
    return info

student_1 = student_info(name="Waqas Ahmad", age=21, city="Abbottabad", semester=5)
print(student_1)
student_2 = student_info(name="Ilyas Khan", age=21, city="Dir lower", semester=4)
print(student_2)




