#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 0.516000032425 seconds.
#

# Description:
# The 5-digit number, 16807=7^(5), is also a fifth power.
# Similarly, the 9-digit number, 134217728=8^(9), is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

numbers = 0

for a in range(1,100):
    for b in range(1,100):
        if len(str(a ** b)) == b:
            numbers += 1
            print (a ** b), a, b

print (numbers)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
