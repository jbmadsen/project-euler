#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-30
# Computation time: 0.890000104904 seconds.
#

# Description:
# A googol (10^(100)) is a massive number: one followed by one-hundred zeros;
# 100^(100) is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a^(b), where a, b < 100,
# what is the maximum digital sum?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

final = 0
for a in range(1,101):
    for b in range(1,101):
        string = str(a**b)
        sum = 0
        for c in string:
            sum += int(c)
        if sum > final:
            final = sum

print (final)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")

