'''
The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
'''

# (1 + 2 + ... + 10)**2 = 55**2 =
def getSum(a):
    # sum of first and last element, multiplied by half the number of elements,
    # squared
    res = ( (a[0]+a[-1]) * (len(a)/2) )**2 
    return res

# gives 3025
#print getSum(range(1,11))

def getMulti(a):
    s = 0 # sum. 
    for i in a:
        s = s + i**2
    return s     

# gives 385
#print getMulti(range(1,11))

print(getSum(range(1,11)) - getMulti(range(1,11)))
#print(getSum(range(1,101)) - getMulti(range(1,101)))
