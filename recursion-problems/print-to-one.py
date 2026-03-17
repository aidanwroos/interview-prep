# print given integer n, print n to 1 without using loops


def recursiveLoop(n):

    # base case
    if n < 1:
        return
    
    # print n before calling recursive function
    print(n)
    
    recursiveLoop(n - 1)
    



recursiveLoop(10)