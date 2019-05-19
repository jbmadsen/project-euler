#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-29
# Computation time: 0.0 seconds.
#

# Description:
# Starting in the top left corner of a 2 x 2 grid,
# there are 6 routes (without backtracking) to the bottom right corner.
#
# How many routes are there through a 20 x 20 grid?

# Imports the math module
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

grid = [20, 20]


# Algorithm ( courtesy of : http://www.joaoff.com/2008/01/20/a-square-grid-path-problem/ )
#           ( m + n )! / m! * n!
def factorial(n):
    tmp_sum = 1
    while n != 0:
        tmp_sum *= n
        n -= 1
    return tmp_sum

print (factorial(grid[0] + grid[1]) / (factorial(grid[0]) * factorial(grid[1])))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
