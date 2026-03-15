# given an integer n, find the first n fibonacci numbers recursively
# The Fibonacci sequence is a series of numbers where each number 
# is the sum of the two preceding ones, usually starting with 0 and 1. 
# It begins 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 and so on


def findFibonacci(int n):

  if n == 0 or n == 1:
    return n



number = 10
print(findFibonacci(number))
