# -*- coding: utf-8 -*-
'''
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
'''

class TriangleNumbers:
    def __init__(self):
        self.triangleNumbers =[1]
        self.iterator=2 
        self.createNewTriangleNumbers(500)
    
    def getNextTriangleNumber(self):
        self.triangleNumbers.append(self.triangleNumbers[-1]+self.iterator)
        self.iterator+=1
        #print("new:",self.triangleNumbers[-1],self.getFactors(self.triangleNumbers[-1]))
        return self.triangleNumbers[-1] 
    
    def createNewTriangleNumbers(self, num):
        for i in range(0,num):
            self.getNextTriangleNumber()
 
    def getFactors(self, num):
        factors=[]
        for i in range(1,num+1):
            if num%i == 0:
                factors.append(i)     
        return factors

def getTriangleNumberWith500Factors(tri, lim):
    while 1: 
        # binary search ish. 
        # if the last triangle number has more factors than the limit
        # we have the wanted triangle number in the list. 
        print(tri.triangleNumbers[-1])
        if len(tri.getFactors(tri.triangleNumbers[-1])) > lim:
            # check the center 
            if len(tri.getFactors(tri.triangleNumbers[len(tri.triangleNumbers)/2]))==lim:
                return tri.triangleNumbers[len(tri.triangleNumbers)/2]
            elif len(tri.getFactors(tri.triangleNumbers[len(tri.triangleNumbers)/2])) > lim:
                tri.triangleNumbers=tri.triangleNumbers[len(tri.triangleNumbers):]
            elif len(tri.getFactors(tri.triangleNumbers[len(tri.triangleNumbers)/2])) < lim:
                tri.triangleNumbers=tri.triangleNumbers[:len(tri.triangleNumbers)]
        # if the last triangle number in the list has less then limit factors.  
        elif len(tri.getFactors(tri.triangleNumbers[-1]+1)) < lim:
            # remove existing numbers with less than limit factors. 
            tri.triangleNumbers = [] 
            # create new triangle numbers 
            tri.createNewTriangleNumbers(len(tri.triangleNumbers))
        # if the last triangle number in the list has limit factors.  
        elif len(tri.getFactors(tri.triangleNumbers[-1])) == lim:
            return tri.triangleNumbers[-1] 
    return "FAIL!"

tri = TriangleNumbers()
res = getTriangleNumberWith500Factors(tri, 10)
print(res, ":", tri.getFactors(res))
#print(getTriangleNumberWith500Factors(tri, 500))
