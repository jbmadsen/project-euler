#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 0.0160000324249 seconds.
#

# Description:
# Euler's Totient function, f(n) [sometimes called the phi function],
# is used to determine the number of numbers less than n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than
# nine and relatively prime to nine, f(9)=6.
#
# n 	Relatively Prime 	f(n) 	n/f(n)
# 2 	1       	        1 	2
# 3 	1,2             	2 	1.5
# 4 	1,3 	                2 	2
# 5 	1,2,3,4             	4 	1.25
# 6 	1,5                 	2 	3
# 7 	1,2,3,4,5,6         	6 	1.1666...
# 8 	1,3,5,7 	        4 	2
# 9 	1,2,4,5,7,8 	        6 	1.5
# 10 	1,3,7,9 	        4 	2.5
# 
# It can be seen that n=6 produces a maximum n/f(n) for n = 10.
# 
# Find the value of n = 1,000,000 for which n/f(n) is a maximum.

# Imports
import math
from prime_generator import generate_primes

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

limit = 10**6
number = 1
# Generating primes until sqrt(limit)
primes = generate_primes(int(math.sqrt(limit)))

# Finds the number of primes that can be multiplied before the number is above limit
for prime in primes:
    if number * prime > limit:
        break
    number *= prime

print (number)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
