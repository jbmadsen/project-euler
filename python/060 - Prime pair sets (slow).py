#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2019-05-09
# Computation time: 115.17142271995544 seconds 
#                   (4.86s to find the anwser, the remaining 110s to check everything else exhaustively)
#

# Description:
# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# 
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# Imports
from prime_generator import generate_primes
import itertools
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Brute force intuition:
# - Generate a list of primes using the sieve
# - Check first two elements a,b, add c if a,b is a prime pair. Add d if a,b,c are pairs, etc.
# - Make sure a < b < c < d < e to speed up
# - Calculate sum for pairs, set as max, and continue
# - On completion, max is the correct answer
# - I do assume this will be slow

list_of_primes = generate_primes(10000)
list_of_primes.remove(2)
list_of_primes.remove(5)

num_combinations = 5
checked_pairs = dict()


def concat(x, y):
    return int("%d%d" % (x, y)) # Fastest (so far)
    #return int(str(x)+str(y)) # Faster
    #return int(x*10**(1+math.floor(math.log10(y)))+y) # Slow


def check_prime(n):
    if n in list_of_primes:
        return True
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True
    

def check_pair(first: int, second: int):
    pair = concat(first, second)
    if pair in checked_pairs:
        return checked_pairs[pair]
    is_prime = check_prime(pair)
    checked_pairs[pair] = is_prime
    return is_prime


def check_pairs(first: int, second: int):
    return (check_pair(first,second) and check_pair(second,first))


def find_pairs():
    max_sum = 9223372036854775807 
    for a in list_of_primes:
        for b in list_of_primes:
            if b <= a:
                continue
            if check_pairs(a,b):
                for c in list_of_primes:
                    if c <= b:
                        continue
                    if (check_pairs(a,c) and check_pairs(b,c)):
                        for d in list_of_primes:
                            if d <= c or a+b+c+d > max_sum:
                                continue
                            if (check_pairs(a,d) and check_pairs(b,d) and check_pairs(c,d)):
                                for e in list_of_primes:
                                    if e <= d or a+b+c+d+e > max_sum:
                                        continue
                                    if (check_pairs(a,e) and check_pairs(b,e) and check_pairs(c,e) and check_pairs(d,e)):
                                        max_sum = a+b+c+d+e
                                        print("One solution:", a, b, c, d, e, ", sum:", max_sum)
                                        return max_sum
    return max_sum


max_sum = find_pairs()
print("Solution:", max_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
