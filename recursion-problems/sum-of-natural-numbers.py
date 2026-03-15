# given a number n, find the sum of the first n natural numbers using recursion


def recursionSum(n):

  # base case
  if n == 0:
    return 0

  # recursive call here
  previous_sum = recursionSum(n-1)

  # add previous sum with next number
  return n + previous_sum



print(recursionSum(3))

# ex output:
# recursionSum(3): waiting for...
#   recursionSum(2): waiting for...
#     recursionSum(1): waiting for...
#       recursionSum(0): (return 0)
#     1 + 0 = 1
#   2 + 1 = 3
# 3 + 3 = 6
