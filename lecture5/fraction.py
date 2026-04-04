class Fraction:
    def __init__(self, x, y):
        self.num = x
        self.denu = y
    def __str__(self):
        '''Object representation: '''
        return "{}/{}".format(self.num, self.denu)
    
    def __add__(self, other):
        '''Here when tow object are called for summation then this magic method is automatically called and code is executed:'''
        numerator = self.num * other.denu + self.denu * other.denu
        denumerator = self.denu * other.denu
        return "{}/{}".format(numerator,denumerator)
    
    def __sub__(self, other):
        '''Here when tow object are called for substraction then this magic method is automatically called and code is executed:'''
        numerator = self.num * other.denu - self.denu * other.denu
        denumerator = self.denu * other.denu
        return "{}/{}".format(numerator,denumerator)
    
    def __mul__(self, other):
        '''Here when tow object are called for multiplication then this magic method is automatically called and code is executed:'''
        numerator = self.num * other.num 
        denumerator = self.denu * other.denu
        return "{}/{}".format(numerator,denumerator)
    
    def __truediv__(self, other):
        '''Here when tow object are called for multiplication then this magic method is automatically called and code is executed:'''
        numerator = self.num * other.denu
        denumerator = self.denu * other.num
        return "{}/{}".format(numerator,denumerator)

frac1 = Fraction(3,4)
frac2 = Fraction(5,6)

print(frac1 + frac2)
print(frac1 - frac2)
print(frac1 * frac2)
print(frac1 / frac2)