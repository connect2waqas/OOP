
university_name = "UOH"
def global_var(uni_name, student):
    return f"University: {uni_name}\nStudent: {student}"

global_1 = global_var(uni_name=university_name,student="Waqas Ahmad")
print(global_1)