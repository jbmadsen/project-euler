#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-02
# Computation time: 21.375 seconds.
#

# Description:
# It was proposed by Christian Goldbach that every odd composite number
# can be written as the sum of a prime and twice a square.
#
#   9 = 7 + 2*1^(2)
#   15 = 7 + 2*2^(2)
#   21 = 3 + 2*3^(2)
#   25 = 7 + 2*3^(2)
#   27 = 19 + 2*2^(2)
#   33 = 31 + 2*1^(2)
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the
# sum of a prime and twice a square?

# Imports
import math
from prime_generator import generate_primes

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Opens the log file and read the data to a list
list_of_primes = generate_primes(1000000)

n = 5

while True:
    if not n in list_of_primes:
        if not any( (n-2*i*i) in list_of_primes for i in range(1,n) ):
            break
    n += 2

print (n)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
