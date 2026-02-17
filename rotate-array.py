# juggling algorithm solution
# O(n) time, O(1) space
import math


array = [1, 2, 3, 4, 5, 6, 7, 8]


def rotate_array(array, d):
  # length of the array
  n = len(array)

  # capture case where # steps > number of elements in array
  d = d % n
  
  # number of cycles determined by gcd of array length and num steps
  c = math.gcd(n, d)

  # process each individual cycle
  for i in range(c):

    # the first element and its index in the cycle
    first_element = array[i]
    first_index = i
    
    # process all elements in the cycle
    while True:

      # calculating index of the next element in the cycle
      next_index = (first_index + d) % n

      # we made it back to the first element, break loop
      if next_index == i:
        break

      # place the element, move first index to next index
      array[first_index] = array[next_index]
      first_index = next_index

    # set first element in the cycle, using first_index
    array[first_index] = first_element

  return array


print(f"Original array: {array}")
print(f"Rotated array: {rotate_array(array, 2)}")
