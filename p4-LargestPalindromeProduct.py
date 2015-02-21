'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import copy

def getNumbersInRange(start, stop):
    # three digit numbers
    # 100 - 999
    # set with all three digit numbers.  
    numbers = set()
    for i in range(start, stop):
        numbers.add(i)
    return numbers
    
# checks is input is a palindrome. 
def isPalindrome(pal):
    if str(pal) == str(pal)[::-1]:
        return True
    return False

    # palindrome testing. 
    #print isPalindrome(9009), " - True"
    #print isPalindrome(90109), " - True"
    #print isPalindrome(9080), " - False"
    #print isPalindrome(90180), " - False"

def getHighestPalindrome(numbers):
    # products that are palindromes. 
    palindromes = set()
    
    # find all palindromes
    numCopy = copy.copy(numbers)
    for a in numCopy:
        numbers.remove(a)
        for b in numbers: 
            if isPalindrome(a*b):
                palindromes.add(a*b)
    
    # return the highest palindrome.
    return sorted(list(palindromes))[-1]

#print getHighestPalindrome(getNumbersInRange(1, 100))
print getHighestPalindrome(getNumbersInRange(100, 1000))
