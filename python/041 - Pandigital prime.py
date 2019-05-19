#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-31
# Computation time: 9.90600013733 seconds.
#

# Description:
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
#
# Done in ?? seconds.
#

#
# We only need to search for a 7 digit (7654321) and below pandigital, as:
# Given a 9-digit pandigital number, the digits add to 45, meaning the number is divisible by 9;
# Given a 8-digit pandigital number, the digits add to 36, meaning the number is divisible by 9;
# thus, the number cannot be prime.
# ( I have no idea where that rule is from, and how it works.. only that it's there )

# Imports
from prime_generator import generate_primes

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Imports the primes
list_of_primes = generate_primes(7654321)

pandigital = [1,2,3,4,5,6,7,8,9]

def to_list(number):
    # Takes a number and returns a list of digits
    tmp_list = []
    string = str(number)
    for a in string:
        tmp_list.append(int(a))
    return tmp_list

primes = []
for x in list_of_primes:
    #if ['0','8','9'].count(str(x)) == 0:
        tmp_list = to_list(x)
        tmp_list.sort()
        if tmp_list == pandigital[:len(tmp_list)]:
            primes.append(x)
            #print x

print (max(primes))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
