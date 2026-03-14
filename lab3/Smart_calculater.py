def smart_calculator(*args):
    result = 0
    for i in args:
        result +=i
    return result

cal_1 = smart_calculator(1,2,3,4,5)
cal_2  = smart_calculator(100,400,500,8000,2000)
print(cal_1)
print(cal_2)