# given a string s, check if s is a palindrome or not
# ex: s = "abba" yes
# ex: s = "abc" no

def palindromeCheck(s):

    left = 0
    right = len(s) - 1
    flag = True

    while left < right:
        if s[left] != s[right]:
            flag = False
            break
        
        left += 1
        right -= 1

    return flag



strs = ["abba", "abc", "mom", "planet", "3334"]
for str in strs:
    print(f"string: {str}, {palindromeCheck(str)}")