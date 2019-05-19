#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.0 seconds.
#

# Description:
# n! means n * (n - 1) * ... * 3 * 2 * 1
#
# Find the sum of the digits in the number 100!

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The number
number = 100

# sums
tmp_sum = 0
final_sum = 0

# Get the sum of 100!
while number != 0:
    if tmp_sum == 0:
        tmp_sum = number
    else:
        tmp_sum *= number
    number -= 1

# Convert to a list
tmp_str = str(tmp_sum)
tmp_list = list(tmp_str)

# Eval the strings induvidually and add them to the final sum
for x in tmp_list:
    final_sum += eval(x)

# Prints the number
print ("The number:", final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
