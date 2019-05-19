#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-29
# Computation time: 0.406000137329 seconds.
#

# Description:
# An irrational decimal fraction is created by concatenating the positive integers:
#
#       0.12345678910(1)112131415161718192021...
#
# It can be seen that the 12^(th) digit of the fractional part is 1.
# 
# If d_(n) represents the n^(th) digit of the fractional part,
# find the value of the following expression.
# 
# d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

string = ''
number = 1
final_sum = 1

while len(string) < 1000000:
    string += str(number)
    number += 1

for x in range(0,7):
    final_sum *= int(string[(1*10**x)-1])

print (final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
