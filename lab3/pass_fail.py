def result():
    marks = int(input("Enter your marks: "))
    if marks >= 50:
        result = "Pass"
    else:
        result = "Fail"
    return result

result_1 = result()
print(f"Result: {result_1}")
result_2 = result()
print(f"Result: {result_2}")

