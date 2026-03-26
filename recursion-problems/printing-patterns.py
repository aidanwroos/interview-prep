#a collection of patterns printed using recursion

def space(n):
    if n == 0:
        return
    print(" ", end="")
    space(n-1)

#print a square
def square(rows, cols, cur_row=0):

    #base case
    if cur_row == rows:
        return
    
    #top and bottom rows
    if cur_row == 0 or cur_row == rows - 1:
        print('@' * cols)

    #middle rows
    else:
        print('@' + ' ' * (cols - 2) + '@')

    #recursive call
    square(rows, cols, cur_row + 1)

def triangle(height, cols, cur_height=0):

    #base case: we've reached the full height of the triangle atp
    if cur_height == height:
        return



    
square(50,80)
# @@@@@@
# @    @
# @    @
# @@@@@@

#    #
#   ###
#  #####
# #######