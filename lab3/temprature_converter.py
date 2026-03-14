def temprature_convertor():
    temp_in_fahrenheit = float(input("Enter temprature in Fahrenheit: "))
    temp_in_calsius = (temp_in_fahrenheit -32) * 5/9
    return temp_in_calsius

temp_1 = temprature_convertor()
print(f"Temprature is: {temp_1:.2f} ℃")
temp_2 = temprature_convertor()
print(f"Temprature is: {temp_2:.2f} ℃")


