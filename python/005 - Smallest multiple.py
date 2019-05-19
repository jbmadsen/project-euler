#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 34.8440001011 seconds.
#

# Description:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

target = 20
counter = 0

while not counter == 19:
    counter = 0
    target += 20
    for x in range(2, 21):
        if target % x == 0:
            counter += 1
        else:
            break

# Prints the number
print ("The number: " + str(target))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
