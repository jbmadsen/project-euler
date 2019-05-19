#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-25
# Computation time: 7.40700006485 seconds.
#

# Description:
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are
# an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110.
# Therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def d(num):
    # Finds all divisors for a number, returning the sum of these
    list_of_divisors = []
    for x in range(1, num // 2 + 1):
        if num % x == 0:
            list_of_divisors.append(x)
    return sum(list_of_divisors)

def amicable(num):
    # Test if a number is amicable
    first_sum = d(num)
    second_sum = d(first_sum)
    if second_sum == num and not first_sum == num:
        return True
    return False

final_sum = 0

# Finds and sums all amicable numbers below 10000
for x in range(1, 10000):
    if amicable(x):
        final_sum += x

# Prints the result
print (final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
