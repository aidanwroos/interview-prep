# given a string, find its length using recursion

def findLength(str):

  # base case, string empty
  if str == "":
    return 0
  
  # recursively call substring, adding 1 to result each time
  # for each character popped from the original string
  return findLength(str[1:]) + 1


str = "Aidan Roos" # length 10
print(findLength(str))
