#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 12.875 seconds.
#

# Description:
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 � 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

pandigital = ['1','2','3','4','5','6','7','8','9']
products = []

def tolist(string):
    # Takes a string and returns the chars in a list
    tmp_str = []
    for x in string:
        tmp_str.append(x)
    tmp_str.sort()
    return tmp_str

for x in range(1,2000):
    for y in range(1,2000):
        tmp_str = str(x) + str(y) + str(x*y)
        if len(tmp_str) == 9:
            alist = tolist(tmp_str)
            if alist == pandigital:
                if not x*y in products:
                    products.append(x*y)
                    print (tmp_str, x, y, x*y)
#print products
print (sum(products))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
