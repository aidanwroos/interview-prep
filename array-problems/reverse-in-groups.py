# Given array arr[] and integer k, find the array after reversing every subarray of
# consecutive k elements in place. If last subarray has fewer than k elements, reverse as is.
# Modify the array in place

array = [1, 2, 3, 4, 5, 6, 7, 8]
#           0-2       3-5      6-7
# list = [ [1,2,3] , [4,5,6] , [7,8] ]

def reverse_in_groups(array, k):

    

    si = 0;  #beginning of array, beginning index of first subarray

    while True:
    
        end_of_subarray = (si + k) - 1

        for i in range(si, (si + k) // 2):
            temp = array[i]
            array[i] = array[end_of_subarray]
            array[end_of_subarray] = temp

            end_of_subarray -= 1
            
        si += k
    


    


    





print(f"Original array: {array}")
reverse_in_groups(array, 3)
print(f"Final array: {reverse_in_groups(array, 3)}")

    