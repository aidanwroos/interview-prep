# given array of integers representing a permutation,
# find the next lexicographically greater permutation.
# If the permutation is alr the greatest, return reversed array
# ex: [2,4,1,7,5,0] -> 2 4 5 0 1 7
# ex: [3,2,1] -> 1 2 3

def nextPermutation(arr):

  pivot_idx = -1     # pivot's index
  successor_idx = 0  # successor's index

  n = len(arr)
  i = 0;

  # determine pivot
  while i < n - 1:
    if arr[i] < arr[i + 1]:
      pivot_idx = i
    i += 1

  # pivot doesn't exist so return reversed array
  if pivot_idx == -1:
    arr.reverse() # (modify's in place, returns None)
    return arr

  # determine successor
  j = pivot_idx

  while j < n:
    if arr[j] > arr[pivot_idx]:
      successor_idx = j
    j += 1

  # swap pivot and successor in place
  temp = arr[pivot_idx]
  arr[pivot_idx] = arr[successor_idx]
  arr[successor_idx] = temp

  # reverse elements to the right of the pivot
  left = pivot_idx + 1
  right = n - 1

  while left < right:
    new_temp = arr[left]
    arr[left] = arr[right]
    arr[right] = new_temp

    left += 1
    right -= 1

  return arr
  

# TEST Permutations
array1 = [2,4,1,7,5,0]
array2 = [1,3,5,4,2]
array3 = [3,2,1]
print(f"Next permutation: {nextPermutation(array1)}")
print(f"Next permutation: {nextPermutation(array2)}")
print(f"Next permutation: {nextPermutation(array3)}")
