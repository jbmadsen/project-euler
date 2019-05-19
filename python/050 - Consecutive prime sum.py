#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-01
# Computation time: 34.1570000648 seconds.
#

# Description:
# The prime 41, can be written as the sum of six consecutive primes:
#
#               41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# Imports
from prime_generator import generate_primes

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Opens the log file and read the data to a list
list_of_primes = generate_primes(1000000)

# Method:
# 1) Create a sequence of all primes under 1000000.
# 2) Start summing elements in the sequence until the next number would put you
#    over 1000000.
# 3) Check if that sum is prime, if not, subtract the last number added.
# 4) Repeat step 3 until you get a prime number, and store it along with the
#    how many consecutive numbers from the original sequence it took to get there.
# 5) Drop the first number from the sequence of primes, and do steps 2-4 again
# 6) Compare the longest chain from the first run with the second run, and store
#    the longer of the two.
# 7) If the sequence of primes is still longer than the longest chain, then
#    repeat steps 5-7...otherwise, you've found the longest sum of consecutive
#    primes!
now = 0
length = 1
result = 0

while now < length:
    tmp = 0
    tmp_len = 0
    for x in range(now, len(list_of_primes)):
        if tmp < 1000000:
            tmp += list_of_primes[x]
            tmp_len += 1
            high = list_of_primes[x]
        if tmp >= 1000000:
            tmp -= list_of_primes[x]
            tmp_len -= 1
            break
    while True:
        if tmp in list_of_primes:
            if tmp_len > length:
                length = tmp_len
                result = tmp
            now += 1
            break
        else:
            tmp_len -= 1
            tmp -= list_of_primes[tmp_len]
    #print now, tmp, tmp_len

print (length, result)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")

