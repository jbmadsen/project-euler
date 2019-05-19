#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 1.67199993134 seconds.
#

# Description:
# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x,
# such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def tolist(number):
    alist = []
    for x in str(number):
        alist.append(x)
    alist.sort()
    return alist

found = False
x = 1

while not found:
    if tolist(2*x) == tolist(3*x) == tolist(4*x) == tolist(5*x) == tolist(6*x):
        print (x)
        found = True
    x += 1

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
