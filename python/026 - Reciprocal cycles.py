#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-27
# Computation time: 41.5629999638 seconds.
#

# Description:
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#   1/2  =  0.5
#   1/3  =  0.(3)
#   1/4  =  0.25
#   1/5  =  0.2
#   1/6  =  0.1(6)
#   1/7  =  0.(142857)
#   1/8  =  0.125
#   1/9  =  0.(1)
#   1/10 =  0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.

# Imports decimal, to enable custom decimal points
import decimal

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Number of the longest recurring cycle
longest = 0

# Set the floating point precision to 2000 after the comma
decimal.getcontext().prec = 2000

def recurrence(string):
    # Find and returns the recurrence cycle of the string
    for a in range(1,len(string)//2+1):
        if len(string[:a]+string[:a]) > 6 and string[:a]+string[:a] in string:
            return string[:a]
    return ''

for x in range(1,1000):
    # How the hell should this be solved?
    tmp_str = str(decimal.Decimal(1) / decimal.Decimal(x))
    decimals = tmp_str[2:]
    if not len(decimals) < 20:
        string = recurrence(decimals)
        if len(string) > longest:
            longest = x

print (longest)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
