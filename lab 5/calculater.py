class Calculator:
    def __init__(self, operand_1, operand_2):
        self.operand_1 = operand_1
        self.operand_2 = operand_2
    
    def add(self):
        return self.operand_1 + self.operand_2
    def substrate(self):
        return self.operand_1 - self.operand_2
    def multiply(self):
        return self.operand_1 * self.operand_2
    def divide(self):
        if self.operand_2 != 0:
            return self.operand_1 / self.operand_2
        else:
            print(f"Denomerater should not be zero: {self.operand_2}")
    def __str__(self):
        return (f"Addition: {self.add()}\n"
                f"substraction: {self.substrate()}\n"
                f"Multiplication: {self.multiply()}\n"
                f"Division: {self.divide():.2f}"
                )
division = Calculator(2,3)
print(division)