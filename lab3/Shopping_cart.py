def checkout(*shopping_List):
    total = 0
    for i in shopping_List:
        total += i
    return total

list_1 = [500, 300, 200]
list_2 = [900,1000,100]

total_1  = checkout(*list_1)
total_2 = checkout(*list_2)

print(f"Total for list_1: {total_1}")
print(f"Total for list_1: {total_2}")

