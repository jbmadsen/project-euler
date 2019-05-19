#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 1.375 seconds.
#

# Description:
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
# is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

# Imports
from decimal import Decimal

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def tolist(string):
    # Takes a string and returns the chars in a list
    tmp_str = []
    for x in string:
        tmp_str.append(x)
    tmp_str.sort()
    return tmp_str

xlist = []
ylist = []

for x in range(10,100):
    for y in range(x+1,100):
        #print "(",x,"/",y,")", Decimal(x)/Decimal(y)
        if len(str(Decimal(x)/Decimal(y))) < 5:
            tmp_x = tolist(str(x))
            tmp_y = tolist(str(y))
            for a in tmp_x:
                if a in tmp_y:
                    tmp_x.remove(a)
                    tmp_y.remove(a)
                    if not a == '0':
                        try:
                            if Decimal(x)/Decimal(y) == (Decimal(tmp_x[0])/Decimal(tmp_y[0])):
                                print ("(",x,"/",y,")", (Decimal(x)/Decimal(y)))
                                xlist.append(x)
                                ylist.append(y)
                        except:
                            pass

tmp = (Decimal(xlist[0]*xlist[1]*xlist[2]*xlist[3])/Decimal(ylist[0]*ylist[1]*ylist[2]*ylist[3]))
print ("Sum of the lowest common terms of the denominators:", 1 / float(tmp))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
