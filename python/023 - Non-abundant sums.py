#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-27
# Computation time: 28.4679999352 seconds.
#

# Description:
# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers. However,
# this upper limit cannot be reduced any further by analysis even though
# it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers
# which cannot be written as the sum of two abundant numbers.

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def divisors(n):
    # Only the square of the number is needed, as the factor pairs below shows
    # the triangular number T(37) has 12 factors which yields
    # the (a,b) pairs 1,666; 2,333; 3,222; 6,111; 9,74 and 18,37.
    # Courtesy of : http://www.physicsforums.com/showthread.php?t=119070
    if n == 2:
        divisor = [1]
        return divisor
    divisor = []
    for x in range(1, math.ceil(n ** 0.5) + 1):
        if n % x == 0:
            if not x in divisor:
                divisor.append(x)
            if not n/x >= n:
                if not n/x in divisor:
                    divisor.append(n/x)
    return divisor

def is_abundant(number, a_list):
    # Returns true if the number is abundant
    if number < sum(a_list):
        return True
    return False

# The variables
numbers = []
abundant_numbers = []

# Array of all numbers
for x in range(1,28124):
    numbers.append(x)

# Array of abundant numbers
for x in range(1,28124):
    if is_abundant(x, divisors(x)):
        abundant_numbers.append(x)

# Set all abundant + abundant sums to 0
for a in range(len(abundant_numbers)):
    for b in range(len(abundant_numbers)):
        tmp = abundant_numbers[a] + abundant_numbers[b]
        if tmp < 28124:
            numbers[tmp-1] = 0

# Print the sum of all the numbers
print (sum(numbers))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
