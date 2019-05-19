#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 14.2030000687 seconds.
#

# Description:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6^(th) prime is 13.
# What is the 10001^(st) prime number? (104743)

#Imports time and start counting
import time, sys
start = time.time()
print ("Starting...")

# The list of the found numbers
list_of_primes = [2,3,5,7]

# Prime generator
for x in range(7, sys.maxsize, 2):
    temp = 0
    if len(list_of_primes) >= 10001:
        break
    for prime in list_of_primes:
        if x % prime == 0:
            temp = 1
            break
    if temp == 0:
        if not x in list_of_primes:
            list_of_primes.append(x)

# Prints the list
print ("10001'st prime number: ", list_of_primes[10000]) # 10001, as 0 is included

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
