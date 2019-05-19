#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.01339999676 seconds.
#

# Description:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The number we are looking below
number = 600851475143

# Try to (evenly) divide our number until the numbers is 0 or 1, 
# checking the divisors at each step for modulus of the number, at which point, we have our factors
def prime_factors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num /= divisor
        divisor = divisor + 1
    return factors

factorsList = prime_factors(number)

# Prints the value (largest prime)
print (max(factorsList))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
