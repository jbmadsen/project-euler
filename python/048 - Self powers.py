#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.077999830246 seconds.
#

# Description:
# The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.
#
# Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The final sum
final_sum = 0

for x in range(1,1001):
    final_sum += x ** x

# Reverse, convert to a list, join to string, cut everything but the first ten,
# reverse again, convert to a list, join to string
tmp_str = str(final_sum)
tmp_str = reversed(tmp_str)
tmp_list = list(tmp_str)
tmp_str = "".join(tmp_list)
tmp_str = tmp_str[:10]
tmp_str = reversed(tmp_str)
tmp_list = list(tmp_str)
tmp_str = "".join(tmp_list)

# Prints the number
print ("The number:", int(tmp_str))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
