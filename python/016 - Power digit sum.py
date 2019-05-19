#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.0159997940063 seconds.
#

# Description:
# 2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^(1000)?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The number
number = 2 ** 1000

# The final sum
final_sum = 0

# Convert to a list
tmp_str = str(number)
tmp_list = list(tmp_str)

# Eval the strings induvidually and add them to the final sum
for x in tmp_list:
    final_sum += eval(x)

# Prints the number
print ("The number:", final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
