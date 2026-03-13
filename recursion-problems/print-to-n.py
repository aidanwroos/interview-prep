# print 1 to n without using any loops


def recursiveLoop(n):

    # base case
    if n == 0:
        return
    
    # call recursive function BEFORE printing value
    recursiveLoop(n-1)

    # print value after recursive function has returned
    print(n)
    


recursiveLoop(10)