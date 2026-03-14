def deposite(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    else:
        balance += amount
    return balance

deposit_1 = deposite(3000,2000)
print(f"Balance after Deposite: {deposit_1}")
deposit_2 = deposite(4000,1000)
print(f"Balance after Deposite: {deposit_2}")
