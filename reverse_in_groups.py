# reverse in groups
# given array arr, and integer value k
# reverse each subarray of size k. If remaining number of elements
# in the array is less than k, reverse elements as is.

array = [7, 2, 3, 8, 9, 4, 5, 6, 1]

def reverse_in_groups(arr, k):

  array_length = len(arr)
  i = 0 # first index of current subarray
  
  
  while (i < array_length):

    left = i
    right = min(array_length - 1, (i + k) - 1)

    while(left < right):
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp

      left += 1
      right -= 1

    i += k
  
  return arr

print(array)
print(reverse_in_groups(array, 4))
