#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.0160000324249 seconds.
#

# Description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The number we are looking below
number = 1000

# The sum of all the numbers added together
final_sum = 0

# The iterator to travel through the numbers
for x in range(number):
    if not x == 0: # 0 is not needed
        if x % 3 == 0 or x % 5 == 0:
            final_sum += x

# Prints the final sum
print (final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
