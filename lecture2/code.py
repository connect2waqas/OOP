print("<===========================Task Number 1")
def grade_system(student,scores):
    for i in range(len(student)):
        if scores[i] >= 90:
            grade = "A"
        elif  (scores[i] >=80) and (scores[i] < 90):
            grade = "B"
        elif (scores[i] >=70) and (scores[i] < 80):
            grade = "C"
        else:
            grade = "F"
        print(f"{student[i]} has got {scores[i]} has grade :{grade}")

student = ["waqas","roman","ilyas","abbas"]
scores = [98,79,56,45,50]
print(grade_system(student,scores))


print("<=============================Task number 2 =====================================>")
def getting_total_inventry(product_name,product_price,product_quantity,treshold):
    for i in range(len(products_price)):
        if len(products_quantity) < 3:
            print(f"{product_quantity[i]} is below the threshold")
        else:
            total_inventry = products_price[i] * products_quantity[i]
            print(f"{products_name[i]}: {total_inventry}")

products_name = ["watches","glasses","shoes"]
products_price = [3000,2000,4000]
products_quantity = [5,6,8]
treshold = 2
getting_total_inventry(products_name,products_price,products_quantity,treshold)
print("<=================== Task ends ============================>")