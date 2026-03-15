# given a string str, print the string in reverse order using recursion

def reverse(str):

  # base case: empty str
  if str == "":
    return ""

  # take off first char, then pass the rest of the string 
  # into next recursive call till base case condition is met
  return reverse(str[1:]) + str[0]



str = "Aidan Is Amazing"
print(reverse(str))
