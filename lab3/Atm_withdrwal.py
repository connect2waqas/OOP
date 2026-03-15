def with_drawl_system(balance, amount):
    threshold = 1000
    if amount <= 0:
        raise ValueError("Amount cannot Zero or less")
    elif balance < threshold:
        print("Balance cannot be less then threshol")
    elif amount == balance:
        print("Balance and withdral amount cannot be same.")
    else:
        if (balance - amount) < threshold:
            print("Amount should be less then threshold")
        else:
            balance -= amount
        return f"balance: {balance}\namount: {amount}"
withdrawl_1 = with_drawl_system(4000,2000)
print(withdrawl_1)