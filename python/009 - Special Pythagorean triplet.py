#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 7.125 seconds.
#

# Description:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^(2) + b^(2) = c^(2)
#
# For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

#Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Method for finding a,b,c
def find_triplets():
    for a in range(150, 700):
        for b in range(150, 700):
            for c in range(150, 700):
                if (a < b < c) and (a + b + c) == 1000 and (a ** 2 + b ** 2 == c ** 2):
                    return [a,b,c]

triplets = find_triplets()
print ("Solution: (", triplets[0], triplets[1], triplets[2], ")")
print ("Product:", triplets[0] * triplets[1] * triplets[2])
                            
# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
