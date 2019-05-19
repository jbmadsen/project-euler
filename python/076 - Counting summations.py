#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2010-09-15
# Computation time: 58.515999794 seconds.
#

# Description:
# It is possible to write five as a sum in exactly six different ways:
#
#   4 + 1
#   3 + 2
#   3 + 1 + 1
#   2 + 2 + 1
#   2 + 1 + 1 + 1
#   1 + 1 + 1 + 1 + 1
#
# How many different ways can one hundred be written as a sum
# of at least two positive integers?

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def combinations(minimum, number):
    # Determines the sum of number of ways to write an integer
    # Using: http://en.wikipedia.org/wiki/Integer_partition
    if number <= 1 or minimum == 2:
        return number // 2 + 1
    elif minimum == 1:
        return 1
    elif number < minimum:
        return combinations(number - 1, number) + 1
    else:
        return sum([combinations(minimum - 1, number - minimum * x) for x in range(number // minimum + 1)])

print (combinations(99,100))
#print (combinations(10,10))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
