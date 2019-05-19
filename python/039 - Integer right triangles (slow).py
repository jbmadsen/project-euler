#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-30
# Computation time: 60.8289999962 seconds.
#

# Description:
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
#       {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?

import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Variable to gather the outputs
results = []
count = 0
number = 0

# c will be greater than a and b
# a and b are interchangable, so to minimize computation, we set a < b
# minimum is a = 1, b = 2, and thus max to count to is 997
# Now just brute-force find a,b,c <= 1000, and count the number of occurences
for a in range(1,997+1):
    for b in range(a,997+1):
        for c in range(b,997+1):
            if (a + b + c <= 1000) and (a*a) + (b*b) == (c*c):
                results.append(a+b+c)

# Get the results and appends them by occurence in a new list                
tmp_list = []
for a in results:
    if not [results.count(a),a] in tmp_list:
        tmp_list.append([results.count(a),a])

# Get the element with highest occurence
for a in tmp_list:
    if a[0] > count:
        count = a[0]
        number = a[1]

# Print occurence and the number
print (count, number)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
