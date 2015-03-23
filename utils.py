import math

'''
Generates prime number under a given higher limit.
@param lim: the higher limit of wanted primes. 
'''
def getPrimes(lim):
    primes = []
    # append the first prime
    primes.append(2)
    #print "primes: ", primes
    # for all numbers below the higher limit. 
    for i in range(3,lim+1,2):
        isPrime = True
        #print "num!",i
        # check the current number against the already registered primes. 
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

