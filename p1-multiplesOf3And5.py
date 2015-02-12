
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The res of these multiples is 23.

Find the res of all the multiples of 3 or 5 below 1000.

'''

def test():
    res=0
    for a in range(1,10):
        if(a % 3 == 0 or a % 5 == 0):
            res+=a
    print "result:",res

def run():
    res=0
    for a in range(1,1000):
        if(a % 3 == 0 or a % 5 == 0):
            res+=a
    print "result:",res

#test()
run()
