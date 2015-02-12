
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

primes = []
checkHigh = 0

def makePrimes(lim):
    for i in range(0,lim):
        isPrime(i)
        #if isPrime(i):
        #    print i

## check if number is a prime. 
def isPrime(num):
    if num == 0: return False
    if num == 1: return False
    if num == 2: return True
    # check the number against the already registered primes. 
    for p in primes:
        #print "--", num, p
        if num % p == 0:
            return False
    primes.append(num)
    return True

def getLargestFactor(num):
    for p in reversed(primes):
        if num % p == 0:
            return p

def getRes(num):
    # get potential primes for num. 
    makePrimes(int(math.ceil(math.sqrt(num))))
    print primes
    # get factors for num. 
    print getLargestFactor(num)

#getRes(13195)
getRes(600851475143)
