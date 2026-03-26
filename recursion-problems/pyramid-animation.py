import os
import time
#Rotating triangle animation using recursive functions to display triangle patterns

#clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#prints a row
def printRow(n):
    if n == 0:
        return
    print("* ", end="")
    printRow(n-1)

#prints pattern facing up
def upside(cols,rows):
    if cols == 0:
        return
    printRow(rows)
    print("\n", end="")
    upside(cols - 1, rows + 1)

#prints pattern facing down
def downside(cols, rows):
    if cols == 0:
        return
    printRow(rows)
    print("\n", end="")
    downside(cols - 1, rows - 1)

#prints upward facing pattern (180 degrees)
def oneighty(n, num):
    if n == 0:
        return
    space(n - 1)
    asterik(num - n + 1)
    print()
    oneighty(n - 1, num)

#prints downward facing pattern (180 degrees)
def oneighty_flipped(n, num):
    if n == 0:
        return
    space(num - n)
    asterik(n)
    print()
    oneighty_flipped(n - 1, num)

#prints asteriks
def asterik(a):
    if a == 0:
        return
    print("*", end=" ")
    asterik(a - 1)

def space(s):
    if s == 0:
        return
    print(" ", end=" ")
    space(s - 1)

#adjustable pyramid rotation period
t = 0.2

#animation loop
while True:
    clear()
    upside(5, 1)

    time.sleep(t)
    clear()

    downside(5, 5)
    time.sleep(t)
    clear()

    oneighty_flipped(5, 5)
    time.sleep(t)
    clear()

    oneighty(5, 5)
    time.sleep(t)
    clear()
    
    
