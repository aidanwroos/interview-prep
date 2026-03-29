import time

# Stupid 67 recursive function

def sixseven(n):
  if n == 0:
    return

  flag = n % 2
  
  if flag == 0:
    print("6", end='')
  else:
    print("7", end=' ')

  sixseven(n-1)


sixseven(20)
