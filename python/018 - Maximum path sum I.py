#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-25
# Computation time: 0.608999967575 seconds.
#

# Description:
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
# 3
# 7 5
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The numbers
numbers = [ [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23] ]

# Algorithm:
# Look at one "sub-triangle" at the bottom such as (the very left one)
#  
#   63
# 04  62
#
# Simply replace 63 with the sum of 63 and the largest
# of its "children" in this case 62. That is we get
#
#   125
# 04   62
#
# Do this for the "sub-triangles" on the last two rows.
# Next move up one row and rinse and repeat.
# When we reach the top we get the result in the top-most cell.

for n in range(len(numbers) - 2, -1, -1):
    for x in range(len(numbers[n])):
        #print (numbers[n][x], max(numbers[n+1][x], numbers[n+1][x+1]))
        numbers[n][x] = numbers[n][x] + max(numbers[n+1][x], numbers[n+1][x+1])

# Prints the number
print (numbers[0][0])  

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
