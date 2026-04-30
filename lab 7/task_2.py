class CreditCard:
    def process_payment(self):
        print("Payments processing through credit card")

class UPI:
    def process_payment(self):
        print("Payments processing through UPI")

class Google_Wallet:
    def process_payment(self):
        print("Payments processing through Google wallet")

methods = [CreditCard(), UPI(), Google_Wallet()]

def payments(obj):
    obj.process_payment()

for method in methods:
    payments(method)


