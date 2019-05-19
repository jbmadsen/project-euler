#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2010-09-15
# Computation time: 0.0 seconds.
#

# Description:
# The first known prime found to exceed one million digits was discovered in 1999,
# and is a Mersenne prime of the form 2^(6972593)-1; it contains exactly 2,098,960 digits.
# Subsequently other Mersenne primes, of the form 2^(p)-1,
# have been found which contain more digits.
#
# However, in 2004 there was found a massive non-Mersenne prime which
# contains 2,357,207 digits: 28433*2^(7830457)+1.
#
# Find the last ten digits of this prime number.

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# pow(x,y,z) is x**y % z, just computed more efficiently
print ((28433*pow(2,7830457, 10**10)+1) % 10**10)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
