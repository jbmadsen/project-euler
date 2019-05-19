#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-03
# Computation time: 0.0780000686646 seconds.
#

# Description:
# It is possible to show that the square root of two can be expressed as an infinite
# continued fraction.
#
# sqrt( 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... )))) = 1.414213...
#
# By expanding this for the first four iterations, we get:
#
#   1 + 1/2 = 3/2 = 1.5
#   1 + 1/(2 + 1/2) = 7/5 = 1.4
#   1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#   1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408,
# but the eighth expansion, 1393/985, is the first example where the number
# of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than denominator?

# Todo:
# Expand the series as 2d + n for the numerator and d+n for the denominator
# and count the number of times the length of the numerator exceeds the
# denominator as strings.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

numerator = 3
denominator = 2
count = 0

for x in range(2,1000):
    tmp_num = numerator
    numerator += (denominator * 2)
    denominator += tmp_num
    if len(str(numerator)) > len(str(denominator)):
        count += 1

print (count)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")

