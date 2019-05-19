#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-07
# Computation time: 4.23399996758 seconds.
#

# Description:
# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
#
#   37 36 35 34 33 32 31
#   38 17 16 15 14 13 30
#   39 18  5  4  3 12 29
#   40 19  6  1  2 11 28
#   41 20  7  8  9 10 27
#   42 21 22 23 24 25 26
#   43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal,
# but what is more interesting is that 8 out of the 13 numbers lying along
# both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with
# side length 9 will be formed. If this process is continued,
# what is the side length of the square spiral for which the ratio of primes
# along both diagonals first falls below 10%?

# The center is always 1
# The ones in the lower left can be found using n ** 2 - (n-1) # n must be odd (1,3,5,7)
# The ones in the lower right can be found using n ** 2 # n must be odd
# The ones in the upper right can be found using n ** 2 - (n-1*3) # n must be odd
# The ones in the upper left can be found using n ** 2 - (n-1*2) # n must be odd

import math
import random

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

primes = 0.0
numbers = 1.0 # 1 init
length = 1.0
percentage = 1.0

########
# I DONT REALLY UNDERSTAND IT...
# http://en.wikipedia.org/wiki/Miller-Rabin_primality_test
# http://en.literateprograms.org/Miller-Rabin_primality_test_%28Python%29
########
def miller_rabin_pass(a, number): #a?
    d = number - 1
    s = 0
    while d % 2 == 0:
        d >>= 1 # Bit shifts, still ?? though
        s += 1
    a_to_power = pow(a, d, number)
    if a_to_power == 1:
        return True
    for _ in range(s-1):
        if a_to_power == number - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % number
    return a_to_power == number - 1

def miller_rabin(number):
    for _ in range(20):
        a = 0
        while a == 0:
            a = random.randrange(number)
        if not miller_rabin_pass(a, number):
            return False
    return True
########
    
# The math can be improved: there's no need to calculate this much
while percentage > 0.10:
    length += 2.0
    if miller_rabin(int(length ** 2 - ((length-1)*3))): # upper right
        primes += 1.0
    if miller_rabin(int(length ** 2 - ((length-1)*2))): # upper left
        primes += 1.0
    if miller_rabin(int(length ** 2 - (length-1))): # lower left
        primes += 1.0
    # Lower right will always be a square, and thus, not a prime
    numbers += 4.0
    percentage = float(primes/numbers)
        
print (int(length), percentage)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
