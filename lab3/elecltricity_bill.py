def calculate_bill():
    units = int(input("Enter number of units: "))
    total_bill = units * 25 
    return total_bill

bill_1 = calculate_bill()
print(bill_1)
bill_2 = calculate_bill()
print(bill_2)