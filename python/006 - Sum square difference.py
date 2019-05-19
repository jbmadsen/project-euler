#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.0 seconds.
#

# Description:
# The sum of the squares of the first ten natural numbers is,
#   1^(2) + 2^(2) + ... + 10^(2) = 385
#
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
#
# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Number
number = 100

# The difference
difference = 0

def sum_of_squares(number):
    temp = 0
    for x in range(number + 1):
        temp += x ** 2
    return temp

def square_of_sum(number):
    temp = 0
    for x in range(number + 1):
        temp += x
    return temp ** 2

sum_of_squares = sum_of_squares(number)
square_of_sum = square_of_sum(number)

difference = square_of_sum - sum_of_squares

# Prints the difference
print ("The difference: " + str(difference))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
