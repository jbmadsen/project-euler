#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2019-05-08
# Computation time: 1.459822654724121 seconds.
#

# Description:
# By replacing the 1^(st) digit of *3, it turns out that six of the nine possible values:
#
#     13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3^(rd) and 4^(th) digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among the
# ten generated numbers, yielding the family: 56003, 56113, 56333, 56443,
# 56663, 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

# Imports
from prime_generator import generate_primes
import collections

# Imports time and start counting
import time
start = time.time() 
print ("Starting...")

list_of_primes = generate_primes(1000000)

# Given how the remainder of the sum of the digits works, we are looking for a three digit replacement
# https://math.stackexchange.com/questions/166800/primality-and-repeated-digits
replace_digits = 3

# As the example has 5 digits, the minimum prime value for an 8 prime family has
# to have at least 6 digits (we assume).
# For that size of prime it would take at least 3 digits to have to be replaced.
# The last digit can't be part of the replacement because that would make it non-prime.
# So we take all 68,906 6-digit primes and reduce it to 5817 by keeping only
# those primes that had 3 or more repeating digits, ignoring the last digit.
# We also remember which digit was repeating so that replacing it will be easy.

large_primes = list(filter(lambda x: x > 100000 and x < 999999 \
    and collections.Counter(str(x)[:-1]).most_common(1)[0][1] >= replace_digits, \
    list_of_primes))
print(len(large_primes))

# We loop through the remaining primes, and using brute-force, we:
# - remove the trailing digit; that never changes
# - check if the count any remaining digit is three (we need only to check 0,1,2 as we need eight, one of them must be)
# - if we find one with count three, we loop through all replacements and check if at least eight of those are prime
# - return at first success 

def is_eight_family(prime: int, index: str):
    c = 0
    for digit in '0123456789':
        n = int(str(prime).replace(str(index), digit))
        if n in large_primes:
            c= c + 1
    return c == 8

def test_index(prime: int, index: int):
    return str(prime)[:-1].count(str(index)) == replace_digits and is_eight_family(prime, index)

for prime in large_primes:
    if test_index(prime, 0) or test_index(prime, 1) or test_index(prime, 2):
        print ("Eight prime family found: ", prime)
        break

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
