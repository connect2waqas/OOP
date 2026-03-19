class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
    def check_balance(self, pin):
        if pin == self.pin:
            print(self.balance)
        else:
            print("Pin not match")
    def deposit(self, amount, pin):
        if pin == self.pin:
            if amount > 0:
                self.balance += amount
            else:
                print("amount should be greater than xero")
        else:
            print("Pin not match!")
        return self.balance
    def withdrawl(self,amount,pin):
        if pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("amount should be less than balance")
        else:
            print("Pin not match")
        return self.balance
        
a = ATM(5000,2004)
a.check_balance(2004)
print(a.deposit(4000,2004))
print(a.withdrawl(1000,2004))
