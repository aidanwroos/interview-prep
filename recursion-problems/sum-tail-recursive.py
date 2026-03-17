# given an array, find the sum of all its elements using tail recursion
# A recursive tail function is one in which the recursive call is the last
# statement that is executed by the function.

# Tail recursion allows for more optimized code done by the compiler. This is
# because since the recursive call is the last statement in the function,
# there's nothing left to do after the call, so saving the current function's stack
# frame can be avoided by sending control back to the beginning of the function
# either by goto or loop statement in the program's assembly

# keep in mind: all the work happens on the way down, not the way up

def tailRecurse(arr, n, sum=0):

  # base case, size is 0 return sum
  if n == 0:
    return sum

  # calculate the new sum
  newSum = sum + arr[n-1]

  # recursive call w/ next array element and new sum
  return tailRecurse(arr, n-1, newSum)
  
  

array = [1,2,3,4,5]
arr_len = len(array)
print(tailRecurse(array, arr_len, 0))

# ex stack trace:
# tailRecurse([1,2,3,4,5], n=5, sum=0) --> 0
#   tailRecurse([1,2,3,4,5], n=4, sum=5) --> 0+5=5
#      tailRecurse([1,2,3,4,5], n=3, sum=9) --> 5+4=9
#         tailRecurse([1,2,3,4,5], n=2, sum=12) --> 9+3=12
#            tailRecurse([1,2,3,4,5], n=1, sum=14) --> 12+2=14
#              tailRecurse([1,2,3,4,5], n=0, sum=15) --> 14+1=15, hit base case, n == 0
#
# every frame now returns 15 to the frame above it, since there's nothing else left to compute
# the print call receives the final frame's return statement, and prints the data!

