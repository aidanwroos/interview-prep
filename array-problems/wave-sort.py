# sort an array in wave form
# wave form: array must follow pattern 
# arr[0] >= arr[1] <= arr[2] >= arr[3] ...

def wave_sort(arr):

  l = len(arr)
  i = 0

  while i < l:
    temp = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = temp

    i += 2

  return arr


array = [1,2,3,4,5,6]

print(array)
wave_sort(array)
print(array)
