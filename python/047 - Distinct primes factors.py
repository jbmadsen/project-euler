#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-02
# Computation time: 24.8280000687 seconds.
#

# Description:
# The first two consecutive numbers to have two distinct prime factors are:
# 
#   14 = 2 * 7
#   15 = 3 * 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
#   644 = 2^2 * 7 * 23
#   645 = 3 * 5 * 43
#   646 = 2 * 17 * 19.
#
# Find the first four consecutive integers to have four distinct primes factors.
# What is the first of these numbers?

# Imports
import math
from prime_generator import generate_primes

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Opens the log file and read the data to a list
list_of_primes = generate_primes(10000)

def factors(number):
    alist = []
    # returns the number of divisible prime factors, returns a list
    for x in list_of_primes:
        if number % x == 0:
            alist.append(x)
    return alist

# Start with the first number that has 4 distinct prime factors.
# Continue to increment from that number until 4 consecutive numbers
# have four distinct prime factors.
c = 1
n = 2*3*5*7 # Lowest number with 4 prime factors
while not c == 4:
    n += 1
    if len(factors(n)) == 4:
        c += 1
    else:
        c = 0

print (n-3) # The first of the four

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
