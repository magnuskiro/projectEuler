'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math
from utils import getPrimes

# test
print "test: ", sum(getPrimes(10))

# run
print "actual: ", sum(getPrimes(2000000))

