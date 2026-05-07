from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def generate_receipt(self):
        pass

class CreditCardPayment(Payment):
    # Fixed: __init__ instead of __int__
    def __init__(self, transaction_id, user_name, balance):
        self.transaction_id = transaction_id
        self.user_name = user_name
        self.balance = balance 
        self.deducted_amount = 0

    def pay(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.deducted_amount += amount
            print(f"PKR{amount} has been paid from {self.user_name}'s Credit Card")
        else:
            print(f"Insufficient balance for {self.user_name}")

    def generate_receipt(self):
        print(f"===Credit Card Receipt ===\nUser: {self.user_name}\nID: {self.transaction_id}\nDeducted: Pkr.{self.deducted_amount}\n")

class JazzCash(Payment):
    def __init__(self, transaction_id, user_name, balance):
        self.transaction_id = transaction_id
        self.user_name = user_name
        self.balance = balance
        self.deducted_amount = 0

    def pay(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.deducted_amount += amount
            print(f"PKR{amount} has been paid via JazzCash for {self.user_name}")
        else:
            print(f"Error: JazzCash account has insufficient funds")

    def generate_receipt(self):
        print(f"JazzCash Receipt:\nUser: {self.user_name}\nTransiction_id: {self.transaction_id}\nPaid: Rs.{self.deducted_amount}\n")

class PayPalPayment(Payment):
    def __init__(self, transaction_id, user_name, balance):
        self.transaction_id = transaction_id
        self.user_name = user_name
        self.balance = balance
        self.deducted_amount = 0

    def pay(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.deducted_amount += amount
            print(f"Rs.{amount} paid via PayPal for {self.user_name}")
        else:
            print(f"balance low for {self.user_name}")

    def generate_receipt(self):
        print(f"PayPal\nUser: {self.user_name}\nRef: {self.transaction_id}\nTotal: Rs.{self.deducted_amount}\n")

creditcardpayment = CreditCardPayment(12345555, "Waqas Khan", 2000)
jazzcash = JazzCash(12345556, "Waqas Khan", 2000)
paypal = PayPalPayment(12345557, "Waqas Khan", 2000)

methods = [creditcardpayment, jazzcash, paypal]

for method in methods:
    method.pay(500)            
    method.generate_receipt()
