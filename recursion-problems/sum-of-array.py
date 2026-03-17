# given an array of integers, find the sum of the array elements using recursion


def sumArray(arr, n):

  if n == 0:
    return 0

  return arr[n-1] + sumArray(arr, n-1)


array = [1,2,3,4,5]
arr_len = len(array)

print(sumArray(array, arr_len))


# ex stack trace:
# sumArray(array, 5)
#   sumArray(array, 4)
#     sumArray(array, 3)
#       sumArray(array, 2)
#         sumArray(array, 1)
#           sumArray(array, 0) (base case)
#         arr[1-1=0] = 1 +
#       arr[2-1=1] = 2 + 
#     arr[3-1=2] = 3 +
#   arr[4-1=3] = 4 +
# arr[5-1=4] = 5 

# 1 + 2 + 3 + 4 + 5 = 15
