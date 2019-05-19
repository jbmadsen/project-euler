#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-10
# Computation time: 0.0310001373291 seconds.
#

# Description:
# Comparing two numbers written in index form like 2^(11) and 3^(7) is not difficult,
# as any calculator would confirm that 2^(11) = 2048 < 3^(7) = 2187.
#
# However, confirming that 632382^(518061) > 519432^(525806) would be much more difficult,
# as both numbers contain over three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'),
# a 22K text file containing one thousand lines with a base/exponent pair on each line,
# determine which line number has the greatest numerical value.

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

numbers = []
highest = [0,0]

# Imports the lines from the file
logfile = open('099 - base_exp.txt', 'r')
while True:
    try:
        numbers.append(list(eval(logfile.readline())))
    except:
        break
logfile.close()

# Two ways to approach this:
# First, pow(x,y,z) is x**y % z, just computed more efficiently
# print pow(632382,518061, 10**10)
# however, this tells only the first 10**10 digits, not the number of digits
# Second, as log(a**x) = x*log(a).. this should work better
for x in numbers:
    tmp = x[1] * math.log(x[0])
    if tmp > highest[0]:
        highest[0] = tmp
        highest[1] = numbers.index(x) + 1 # +1 is needed, as list starts as 0

print (highest)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
