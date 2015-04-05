'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math

def getPythagoreanTriplet(a, b, c):
    if a > b or b > c:
#        print("check: a>b>c", a,b,c)
        return False
    if (a**2 + b**2) != c**2:
#        print("check: (a**2 + b**2)",a,b,c)
        return False
    if a+b+c != 1000:
#        print("check: 1000",a,b,c)
        return False 
    return True 

def getC(a, b):
    return 1000-a-b

#print(getC(3, 4))

def testAll():
    for a in range(1,600):
        for b in range(a,600):
            if getPythagoreanTriplet(a, b, getC(a,b)):
                print("sum:",a*b*getC(a,b),";", a,b,getC(a,b), ";", a+b+getC(a,b))
testAll()

