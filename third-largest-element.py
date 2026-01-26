# find the 3rd largest element in an un-sorted array of distinct elements

def third_largest_element(arr):

    first_largest = -1
    second_largest = -1
    third_largest = -1

    for i in range(0, len(arr)):
        
        if arr[i] > first_largest:
            third_largest = second_largest
            second_largest = first_largest
            first_largest = arr[i]

        elif arr[i] > second_largest:
            third_largest = second_largest
            second_largest = arr[i]

        elif arr[i] > third_largest:
            third_largest = arr[i]

    return third_largest




array = [1, 14, 2, 16, 10, 20]
print(f"Array: {array}")
print(f"Third largest element: {third_largest_element(array)}")
# expecting answer 14