# reverse an array (first element becomes last, and vice-versa)
# (two pointer swap approach)

def reverse_array(arr):

    ptr2 = len(arr) - 1  #end of the array

    for i in range(0, len(arr) // 2):
        temp = arr[i]
        arr[i] = arr[ptr2]
        arr[ptr2] = temp

        ptr2 -= 1
        
    return arr


array = [1, 4, 3, 2, 6, 5, 0, 2, 7, 1, 3]
print(f"Original: {array}")
print(f"Reverse: {reverse_array(array)}")
