# import datetime
# class Transiction:

#     def __init__(self,amount,transiction_type):
#         self.amount = amount
#         self.transiction_type = transiction_type
#         self.timestamp = datetime

#     def __str__(self):
#         if self.transiction_type == "Deposit":
#             return f"Deposit +${self.amount} | {self.timestamp.now()}"
#         elif self.transiction_type == "withdraw":
#             return f"Withdraw: +${self.amount} | {self.timestamp.now()}"
#         else:
#             return "No transictions made."
        
# trans_1 = Transiction(50000,"deposit")
# trans_2 = Transiction(2000,"withdraw")
# class BankAccount:
    
#     def __init__(self, account_number):
#         self._balance = 0.0
#         self._account_number = account_number
#         self._transictions = []
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             self._transictions.append(trans_1)
#         else:
#             print("Wrong amount")
#     def withdraw(self, amount):
#         if amount > 0 and amount < self._balance:
#             self._balance -= Transiction(amount,"withdraw")
#             self._transictions.append()
#         else:
#             print("Wrong amount")
#     def get_balance(self):
#         return f"Balance: ${self._balance}"
    
#     def transictions_history(self):
#         for transiction in self._transictions:
#             print(transiction)
    
# b1 = BankAccount("23422")
# b1.deposit(5000)
# print(b1.transictions_history())


