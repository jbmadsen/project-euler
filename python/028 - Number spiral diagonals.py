#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-25
# Computation time: 0.0149998664856 seconds.
#

# Description:
# Starting with the number 1 and moving to the right in a
# clockwise direction a 5 by 5 spiral is formed as follows:
#
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
#
# It can be verified that the sum of both diagonals is 101.
#
# What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# HINT: 
# The number in the top right corner is n^2,
# the other corners are given by: n^2-n+1, n^2-2n+2, and n^2-3n+3.
# 1, odds 3-500 for (n^2), (n^2-n+1), (n^2-2n+2), and (n^2-3n+3)

diagonal = 1
n = 3

for x in range(1, 501):
    diagonal += n ** 2                  # top right corner
    diagonal += n ** 2 - n + 1          # top left corner
    diagonal += n ** 2 - (2 * n) + 2    # lower left corner
    diagonal += n ** 2 - (3 * n) + 3    # lower right corner
    n += 2

print (diagonal)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
