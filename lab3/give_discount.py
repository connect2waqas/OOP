def final_price(amount):
    threshold = 1000
    if amount < threshold:
        total_price = amount
    else:
        total_price = amount - (amount/10)
    return total_price

    
discount_1 = final_price(2000)
print(f"Total price after discount is : {discount_1}")
discount_2 = final_price(5000)
print(f"Total price after discount is : {discount_2}")
