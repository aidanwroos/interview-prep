# convert a given decimal number n to its equivalent binary number (base 2)


def recursiveConvert(d):

  # base case (when decimal becomes 0)
  if d == 0:
    return 0

  # shift remainder to the left of previous return
  return (d % 2) + 10 * recursiveConvert(d // 2)
  


decimal = 12
print(recursiveConvert(decimal))


# ex stack trace:
# recursiveConvert(10//2 = 5)
#   recursiveConvert(5//2 = 2)
#     recursiveConvert(2//2 = 1)
#       recursiveConvert(1//2 = 0) (base case, when decimal gets divided down to 0, not remainder 0 fyi)
#       1 + 10*0 = 1+0 = 1
#      0 + 10*1 = 0+10  = 10
#    1 + 10*10 = 1+100  = 101
#  0 + 10*101 = 0+1010  = 1010
