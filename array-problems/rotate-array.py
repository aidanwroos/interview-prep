# given array of integers arr[], rotate elements to the left
# by d positions
# juggling algorithm O(n)

# the main idea:
# we're going to rotate the array through cycles. Each cycle
# is independent of one another.
# For any index i in the array, after the rotation we will
# have arr[(i + d) % n] at index i and so on

# How many independent cycles?
# If array of size n is rotated by d places, the number
# of independent cycles is gcd(n, d).

# Number of elements in each cycle?
# Distance travelled in each cycle is a multiple of n defined as
# lcm(n, d)
# So number of elements in each cycle = lcm(n, d) / d.

# To cover all n elements, total number of cycles is n * lcm(n, d)/d = gcd(n, d)

import math


array = [1, 2, 3, 4, 5, 6]


def rotate_array_left(array, d):

    array_length = len(array)

    # case if number of rotations d is > than array length
    if(d > array_length):
        d = d % array_length

    # calulate number of independent cycles
    c = math.gcd(array_length, d)


    # process each individual cycle
    for i in range (0, c):

        # first element in the cycle
        starting_element = array[i]

        # index of first element in current cycle
        currentIdx = i

        # next element index
        nextIdx = 0

        # process all elements in the cycle
        while True:
            # next element in the cycle
            nextIdx = (currentIdx + d) % array_length

            # did full rotation, cuz we reached the starting index again
            if(nextIdx == i):
                break
            
            # update the next index w/ current element
            array[currentIdx] = array[nextIdx]
            currentIdx = nextIdx

        array[currentIdx] = starting_element

    return array

 
def rotate_array_right(array, d):

    n = len(array)

    d = d % n

    c = math.gcd(d, n)

    for i in range(0, c):
        
        




print(f"Original: {array}")
print(f"Rotated left: {rotate_array_left(array, 2)}")
print(f"Rotated right: {rotate_array_right(array, 2)}")