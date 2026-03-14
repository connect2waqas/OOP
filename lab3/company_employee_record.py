def employee_record(name, skills, details):
    print(f"employee name : {name}")
    print("Skills: ")
    for skill in skills:
        print(skill)
    for key, value in details.items():
        print(f"{key} : {value}")

employee_record_1 = employee_record("waqas",skills=["Ai","ML","Python"],details={"age": 24,"city": "islamabad"})
print(employee_record_1)