# given string s, reverse the words in the string
# ex: aidaniscool -> loocsinadia

def reverseString(s):

    #convert string to list
    s = list(s) 

    #maintain left and right ptrs
    left = 0
    right = len(s) - 1
    
    #swap characters at left and right indexes
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
    
        left += 1
        right -= 1
    
    #join resulting list into string again
    return ''.join(s)


str = "aidaniscool"
print(f"{str} -> {reverseString(str)}")