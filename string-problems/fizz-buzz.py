# Fizz Buzz
# Given int n, for every possible integer i <= n, print:
# - "FizzBuzz" if number divisible by 3 and 5
# - "Fizz" if number divisible by 3
# - "Buzz" if number divisible by 5

# FizzBuzz HashMap approach
def fizzbuzz(n):

  result = []

  hash_map = {3 : "Fizz", 5 : "Buzz"}

  divisors = [3,5]

  for i in range(1, n+1):
    temp_res = []

    # iterate through the divisors
    for d in divisors:

      # current integer is divisible by 3 or 5
      if i % d == 0:
        temp_res.append(hash_map[d])
    
    # string is empty, not divisible by 3 or 5
    if not temp_res:
      temp_res.append(str(i))
  
    # append final string to result
    result.append("".join(temp_res))
  
  return result


n = 20
print(f"result: {fizzbuzz(n)}")
