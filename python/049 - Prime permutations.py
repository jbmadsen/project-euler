#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-02
# Computation time: 3.81299996376 seconds.
#

# Description:
# The arithmetic sequence, 1487, 4817, 8147, in which each of the
# terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

# Imports
from prime_generator import generate_primes

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Opens the log file and read the data to a list
list_of_primes = generate_primes(10000)

def is_permutations(a,b,c):
    # Takes three numbers and test if they are permutable of eachother, returns bool
    a, b, c = str(a), str(b), str(c)
    a_list, b_list, c_list = [], [], []
    if not len(a) == len(b) == len(c):
        return False
    for x in range(len(a)):
        a_list.append(a[x])
        b_list.append(b[x])
        c_list.append(c[x])
    a_list.sort()
    b_list.sort()
    c_list.sort()
    if a_list == b_list == c_list:
        return True
    return False

a = 1487+2 # Start one odd above the one in the assignment
while True:
    b, c = a + 3330, a + 6660
    if a in list_of_primes:
        if b in list_of_primes:
            if c in list_of_primes:
                if is_permutations(a,b,c):
                    break
    a += 2

print (str(a)+str(b)+str(c))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
