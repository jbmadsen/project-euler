#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 22.4530000687 seconds.
#

# Description:
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?

# Imports the math module
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

counter = 0
best_start = 0

for x in range(999999, 500000, -2):
    tmp_number = x
    tmp_counter = 0
    while not tmp_number == 1:
        #print tmp_counter, tmp_number
        if tmp_number % 2 == 0:
            tmp_number = tmp_number / 2
            tmp_counter += 1
        else:
            tmp_number = (tmp_number * 3) + 1
            tmp_counter += 1
    if tmp_counter > counter:
        counter = tmp_counter
        best_start = x
        #print best_start, counter

# Print when done
print ("Winner:", best_start, "(", counter, ")")

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
