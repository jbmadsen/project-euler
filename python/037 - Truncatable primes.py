#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 2.60899996758 seconds.
#

# Description:
# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# Import primes generator
from prime_generator import generate_primes 

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

list_of_primes = generate_primes(1000000) # I assume it is less than a million

primes = []

for prime in list_of_primes:
    if prime > 30:
        if '0' in str(prime) or '2' in str(prime):
            pass
        elif '4' in str(prime) or '6' in str(prime) or '8' in str(prime):
            pass
        else:
            primes.append(prime)
    else:
        primes.append(prime)

primes.sort()
#print primes

first_list = []
second_list = []
final = []

for prime in primes:
    length = len(str(prime))
    first = False
    second = False
    if prime > 10:
        len_a = 1
        len_b = 1
        for a in range(1,length):
            if int(str(prime)[a:])in primes:
                len_a += 1
            else:
                break
            if int(str(prime)[:length-a])in primes:
                len_b += 1
            else:
                break
        if len_a == length:
            first = True
        if len_b == length:
            second = True
    if first and second:
        final.append(prime)

print (sum(final))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
