#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.077999830246 seconds.
#

# Description:
# The Fibonacci sequence is defined by the recurrence relation:
#
#    F(n) = F(n-1) + F(n-2), where F(1) = 1 and (2) = 1
#
# Hence the first 12 terms will be:
#
#    F(1) = 1
#    F(2) = 1
#    F(3) = 2
#    F(4) = 3
#    F(5) = 5
#    F(6) = 8
#    F(7) = 13
#    F(8) = 21
#    F(9) = 34
#    F(10) = 55
#    F(11) = 89
#    F(12) = 144
#
# The 12th term, F(12), is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Variables
fibonacci = [1,1]
term = 2 # Nth Fibonacci term

while fibonacci[term - 1] < (10 ** 999):
    fibonacci.append( fibonacci[term - 1] + fibonacci[term - 2] )
    term += 1
    #print fibonacci[term - 1]

# Prints the number
print (term, fibonacci[term - 1])

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
