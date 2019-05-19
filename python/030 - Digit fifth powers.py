#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-25
# Computation time: 7.26600003242 seconds.
#

# Description:
# Surprisingly there are only three numbers that can be written as
# the sum of fourth powers of their digits:
#
#    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
#    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
#    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)
#
# As 1 = 1^(4) is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def digits(num):
    # Splits a number into individual digits
    digits = []
    for n in range(len(str(num))):
        digits.append(int(str(num)[n]))
    return digits

def sumofdigits(digit, power):
    # Returns the sum of the digits in the power
    tmp_sum = 0
    for n in digit:
        tmp_sum += n ** power
    return tmp_sum

final_sum = 0

for x in range(2,500000):
    if x == sumofdigits(digits(x), 5):
        final_sum += x

print ("Sum:", final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
