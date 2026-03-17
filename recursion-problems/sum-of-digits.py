# given a number n, find the sum of its digits using recursion


def digiSum(n):

  # base case, (one digit left)
  if n == 0:
    return 0

  # recursively pass number w/ 1 less digit
  # and add the digit 
  return digiSum(n // 10) + (n % 10)



number = 1234
print(digiSum(number))


# ex stack trace:
# digiSum(1234)
#   digiSum(123)
#     digiSum(12)
#       digiSum(1) --> base case (because single digit 1 // 10 == 0)
#       1%10 = 1 +
#     12%10 = 2 +
#   123%10 = 3 + 
# 1234%10 = 4 +

# 1 + 2 + 3 + 4 = 10
