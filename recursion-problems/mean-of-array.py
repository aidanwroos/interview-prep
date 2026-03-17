# given an array of integers, determine the mean of the array


def mean(arr, n):
  
  # base case: one element, mean is itself
  if n == 1:
    return arr[0]

  # get previous means of first n-1 elements
  prev_mean = mean(arr, n-1)

  return (prev_mean * (n-1) + arr[n-1]) / n


array = [1,2,3,4,5]
arr_len = len(array)

print(mean(array, arr_len))

# ex stack trace:
# mean(arr, 5) waits for...
#   mean(arr, 4) waits for...
#     mean(arr, 3) waits for...
#       mean(arr, 2) waits for...
#         mean(arr, 1) → returns 1.0
#       → (1.0 × 1 + 2) / 2 = 1.5
#     → (1.5 × 2 + 3) / 3 = 2.0
#   → (2.0 × 3 + 4) / 4 = 2.5
# → (2.5 × 4 + 5) / 5 = 3.0 
