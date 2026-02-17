# second largest element
# return second largest element in array
# (One-pass solution)

def second_largest_element(arr):
  largest = -1
  second_largest = -1

  for i in range(len(arr)):
    if arr[i] > largest:
      largest = arr[i]

    if arr[i] < largest and arr[i] > second_largest:
      second_largest = arr[i]

  return second_largest



array = [12, 35, 1, 10, 34, 1]
print(f"Array: {array}")
print(f"Second largest element: {second_largest_element(array)}")