# check whether or not a given string is a palindrome implement using recursion only

def palindrome(string,l,r):

  if l >= r:
    return True

  if string[l] != string[r]:
    return False


  return palindrome(string, l+1, r-1)


#string to test
s = "abba"

print(palindrome(s, 0, len(s)-1))


# stack trace

# palindrome("abba", 0, 3) cmp(a,a) yes
#   palindrome("abba", 1, 2) cmp (b,b) yes
#     palindrome("abba", 2, 1) cmp (b,b), 2 >= 1 return True

# exits program, and doesn't call recursive function again
