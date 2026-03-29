#convert string to integer

#ex "1234" -> 1234

def strToint(s, i):

  if i == len(s): #index reached end of string
    return 0

  digit = int(s[i])

  return digit * (10 ** (len(s) - i - 1)) + strToint(s, i + 1)


print(f"{strToint("1234", 0)}")

# stack trace:

# strtoint("1234", 0) -> 1 * (10 ** (4 - 0 - 1)) +  #1*(10**3) -> 1*1000  = 1000
#   strtoint("1234", 1) -> 2 * (10 ** (4 - 1 - 1)) + #2*(10**2) -> 2*100  = 200
#     strtoint("1234", 2) -> 3 * (10 ** (4 - 2 - 1)) + #3*(10**1) -> 3*10 = 30
#      strtoint("1234", 3) -> 4 * (10 ** (4 - 3 - 1)) + #4*(10**0) -> 4*1 = 4

# 1000 + 200 + 30 + 4 = 1234
