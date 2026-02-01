""""
INHERITANCE POLYMORPHISM
LEARN BY DOING! 
"""
# EXERCISE 1: Empolyee managment system:
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary
    def calculate_salary(self):
        return self.base_salary
    def get_details(self):
        return f"ID : {self.emp_id}, Name: {self.name}"
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus
    def calculate_salary(self):
        """Full-time get base salary and bonus also"""
        return self.base_salary + self.bonus
class PartTimeEmployee(Employee):
    def __init__(self,name, emp_id,hourly_rate,hours_worked):
        super().__init__(name,emp_id, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
class Contractor(Employee):
    def __init__(self, name, emp_id, project_fee, tax_rate):
        super().__init__(name,emp_id,0)
        self.project_fee = project_fee
        self.tax_rate = tax_rate
    def calculate_salary(self):
        return self.project_fee -(self.project_fee * self.tax_rate)
employees = [
    FullTimeEmployee("Waqas khan","F2424",1000000,200000),
    PartTimeEmployee("Ilyas khan","F2020",4000,8),
    Contractor("Bashir","F4242",200000,0.15)
]
# Process payroll - THIS IS POLYMORPHISM IN ACTION!
print("\n Payroll processing:")
total_payroll = 0
for emp in employees:
    salary = emp.calculate_salary()
    total_payroll += salary
    print(f"{emp.get_details()}")
    print(f"  Type: {emp.__class__.__name__}")
    print(f"  Salary: ${salary:,.2f}")
    print()
print(f"Total Payroll: ${total_payroll:,.2f}\n")