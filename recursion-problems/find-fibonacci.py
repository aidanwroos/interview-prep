# given an integer n, find the first n fibonacci numbers recursively
# The Fibonacci sequence is a series of numbers where each number 
# is the sum of the two preceding ones, usually starting with 0 and 1. 
# It begins 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 and so on


def findFibonacci(n):

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return findFibonacci(n-2) + findFibonacci(n-1)


answer = []
number = 20
for i in range(number):
  answer.append(findFibonacci(i))

for a in answer:
  print(a, end=' ')
