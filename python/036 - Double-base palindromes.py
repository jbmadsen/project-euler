#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-25
# Computation time: 6.875 seconds.
#

# Description:
# The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

final_sum = 0

def ispalindromic(num):
    # Checks if a number is palindromic, returns bool
    tmp_str = str(num)
    tmp_rev = reversed(tmp_str)
    tmp_list = list(tmp_rev)
    tmp_rev = "".join(tmp_list)
    if tmp_str == tmp_rev:
        #print tmp_str, tmp_rev
        return True
    else:
        return False

# Loops through a million, finding palindome numbers and sums them
for x in range(1, 1000000):
    if ispalindromic(x) == True:
        base2_number = int(bin(x)[2:])
        if ispalindromic(base2_number) == True:
            #print x, base2_number
            final_sum += x

print (final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
