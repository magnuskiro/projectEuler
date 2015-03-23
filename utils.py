import math

def getPrimes(lim):
    primes = []
    primes.append(2)
    #print "primes: ", primes
    for i in range(3,lim+1):
        isPrime = True
        #print "num!",i
        # check the number against the already registered primes. 
        for p in primes:
            #print "--", i, p
            # if the current modulo prime == 0, it means that current is not a
            # prime
            if i % p == 0:
                isPrime = False
                break
        if isPrime:
            #print "----add", i
            primes.append(i)
    return primes 

