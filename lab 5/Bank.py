class BankAccount:
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print(f"amount should greater than Zero")
    def withdrawl(self, with_drawl_amount):
        if self.balance > with_drawl_amount > 0:
            self.balance -= with_drawl_amount
        else:
            print("Withdrwal amount should be greater than xero and less than balance")
        return self.balance
    def check_balance(self):
        return self.balance
    def __str__(self):
        return (f"Name : {self.name}\n"
                f"Balance: {self.balance}\n"
                f"withdrwal balance: {self.withdrawl(1000)}\n"
                f"check balance: {self.check_balance()}")
account_1 = BankAccount("waqas",40000)
print(account_1)
