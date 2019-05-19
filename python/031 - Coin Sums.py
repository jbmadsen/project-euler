#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 0.0150001049042 seconds.
#

# Description:
# In England the currency is made up of pound, £, and pence, p,
# and there are eight coins in general circulation:
#
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2*20p + 1*5p + 1*2p + 3*1p
#
# How many different ways can £2 be made using any number of coins?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def coins(n):
    count = 0
    for a in range(n, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for _ in range(f, -1, -2):
                                count += 1
    return count

print (coins(200))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
