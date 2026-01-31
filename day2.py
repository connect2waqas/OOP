import random
class BankAccount:
    bank_name = "My_bank"
    total_accounts = 0
    def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts +=1
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
    def display_info(self):
        account_details = [BankAccount.bank_name,self.account_number,self.account_holder,self.get_balance()]
        return account_details
    @classmethod
    def create_accounts(cls,account_holder,initial_deposit):
        account_number = random.randint(1000,5000)
        cls.total_accounts +=1
        return cls(account_number,account_holder,initial_deposit)
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    @staticmethod
    def is_valid_amount(amount):
        return True if amount > 0 else False
class SavingAccount(BankAccount):
    minimum_balance = 1000
    def __init__(self, account_number, account_holder, balance, interest_rate = 0.035):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self,time):
        interest = self.interest_rate * self.balance * time
        self.balance += interest
        return self.balance
    def withdraw(self, amount):
        current_amount = self.get_balance()
        if current_amount < SavingAccount.min_balance:
            print("Witdrawal denied due to Insuffienct balance")
        else:
            current_amount += amount
        return current_amount
acc1 = BankAccount(2342,"waqas khan",9000)
acc2 = BankAccount.create_accounts("Ilyas",90000)
print(acc2.account_holder,acc2.account_number,acc2.balance)
saving1 = SavingAccount(2442,"Waqas khan",1000,)
print(saving1.add_interest(4))

