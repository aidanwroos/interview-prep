# factorial of a number. given the non-negative integers n, compute the factorial
# of a given number.

# note: factorial of n is defined as n * (n-1) * (n-2) * (n-3) * ...
# ex: n=4: 4!= 4 * 3 * 2 * 1 = 24


def findFactorial(n):

  # base case, if n = 0
  if n == 0:
    return 1

  return (findFactorial(n-1) * n)


num = 4
print(findFactorial(num))

# ex stack trace:
# findFactorial(4)
#   findFactorial(3)
#     findFactorial(2)
#       findFactorial(1)
#         findFactorial(0) --> return 1
#       1 * 1 = 1
#      2 * 1 = 2
#     3 * 2 = 6
#    4 * 6 = 24 --> final return statement, res = 24

# print(24) to screen
