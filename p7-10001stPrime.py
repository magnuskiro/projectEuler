'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001th prime number?
'''

###! - copied from p3
primes = []

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
###!

# prime limits.
#a = 6
a = 10001

i = 0 # counter
while len(primes) < a:
    isPrime(i)
    i += 1

print(primes[-1])

