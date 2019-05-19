#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-30
# Computation time: 0.969000101089 seconds.
#

# Description:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Imports the math module
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Function to generate the primes
def generate_primes(n):
    # Sieve Of Eratosthenes
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
    return [i for i in range(2, len(prime)) if prime[i] == True]

# Prints the sum
print(sum(generate_primes(2000000)))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
