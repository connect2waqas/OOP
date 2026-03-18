class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def salary_increase(self, percents):
        if percents < 0:
            print("Percent cannot be negative")
            return self.salary
        if percents > 1:
            percents /= 100
        self.salary += self.salary * percents
        return self.salary
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Current salary: {self.salary}\n"
                f"Increase in salary: {self.salary_increase(20)}"
        )
employee_1 = Employee("waqas", 40000)
print(employee_1)