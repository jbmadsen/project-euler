#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-01
# Computation time: 0.265000104904 seconds.
#

# Description:
# There are exactly ten ways of selecting three from five, 12345:
#
#       123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, ^(5)C_(3) = 10.
#
# In general: ^(n)C_(r) = n!/(r!(n-r)! ,
# where r <= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.
#
# It is not until n = 23, that a value exceeds one-million: ^(23)C_(10) = 1144066.
#
# How many, not necessarily distinct, values of ^(n)C_(r), for 1 = n = 100,
# are greater than one-million?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def factorial(n):
    # Returns the factorial of n
    tmp_sum = 1
    while n != 0:
        tmp_sum *= n
        n -= 1
    return tmp_sum

number = 0 

for n in range(1,101):
    for r in range(n,0,-1):
        tmp = factorial(n) / (factorial(r) * factorial(n-r))
        if tmp > 1000000:
            number += 1

print (number)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
