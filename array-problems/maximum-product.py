# maximum product of a triplet
# given an integer array of either or both positive and negative numbers,
# find a maximum product of a triplet in the array

import math

def maxProduct(array):

  maxA = 0
  maxB = 0
  maxC = 0

  minA = 0
  minB = 0

  for i in range(0, len(array)):

    # largest integer
    if(array[i] > maxA):
      maxC = maxB
      maxB = maxA
      maxA = array[i]

    # second largest integer
    elif(array[i] > maxB):
      maxC = maxB
      maxB = array[i]

    # third largest integer
    elif(array[i] > maxC):
      maxC = array[i]

    # smallest integer
    if(array[i] < minA):
      minB = minA
      minA = array[i]
    
    # second smallest integer
    elif(array[i] < minB):
      minB = array[i]


  return max(minA * minB * maxA, maxA * maxB * maxC)

# One or the other cases will produce a maximum product
# case 1: (minA * minB * maxA)   **note: the two mins could be negative, multiplied to give 
#                                  a positive result possibly swaying the final answer
# case 2: (maxA * maxB * maxC)


array = [-10, -3, 5, 6, -20]
print(f"Max product: {maxProduct(array)}")
