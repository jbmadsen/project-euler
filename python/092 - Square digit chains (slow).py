#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 93.1719999313 seconds.
#

# Description:
# A number chain is created by continuously adding the square of the digits in a number
# to form a new number until it has been seen before.
#
# For example,
#
#   44 -> 32 -> 13 -> 10 -> 1 -> 1
#   85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

one = 0
eightynine = 0
squares = [(x*x) for (x) in range(10)] # [0, 1, 4 .. 81] 
array = []
tid = 10

def one_or_89(n):
    if n == 0:
        return 0
    while n != 89 and n != 1:
        n = sum(squares[int(x)] for x in str(n))
    return n

for x in range(9**2*7+1): # As the higest number possible is 9999999 (9*7)
    array.append(one_or_89(x))

for x in range(1,10**7):
    tmp = array[sum(squares[int(n)] for n in str(x))]
    if tmp == 89:
        eightynine += 1
    #if tmp == 1:
    #    one += 1
    if time.time()-start > tid:
        print (time.time()-start)
        tid += 10
        print (x)

print (eightynine) #"(1, 89):", one, eightynine

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
