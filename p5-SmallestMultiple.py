'''
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''
# get number that is evenly divisible by numbers in range. 
def getNumber(low, high):
    current = 0
    while 1:
        current = current + high 
        div = False
        # check to see if the division if possible for this number. 
        for i in range(low, high+1)[::-1]: # reversed range. 
            div = True
            # if division is not 0, current is not applicable. 
            if current % i != 0:
                div=False
                #print "next"
                break
        # if all modulo divisions are 0 print current number, and exit. 
        if div:
            print("Finished: ", current)
            exit()
        #print current

getNumber(1,10)
#getNumber(1,20)

