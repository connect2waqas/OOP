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
        return cls(account_number,account_holder,initial_deposit)
    
acc1 = BankAccount(2342,"waqas khan",9000)
acc2 = BankAccount.create_accounts("Ilyas",90000)
print(acc2.account_holder,acc2.account_number,acc2.balance)
