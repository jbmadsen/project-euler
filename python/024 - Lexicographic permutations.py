#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-26
# Computation time: 41.3899998665 seconds.
#

# Description:
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
#       012   021   102   120   201   210
#
# What is the millionth lexicographic permutation
# of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# INFO:
# For N objects, the number of permutations is N! (N factorial, or 1 * 2 * 3 * ... N)
# Possible algorithms: http://www.bearcave.com/random_hacks/permute.html

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Variables
list_of_permutes = []
value = [0,1,2,3,4,5,6,7,8,9]
count = 0

def permutation(v, start, n):
    # Permutation implementation
    if start == n-1:
        global count
        count += 1

        string = ''
        for x in range(n):
            string += str(v[x])
        
        global list_of_permutes
        #list_of_permutes.append(v) # For some reason, this always returns [0,1,2,3,4,5,6,7,8,9]
        list_of_permutes.append(string)
    else:
        for i in range(start, n):
            tmp = v[i]
            v[i] = v[start]
            v[start] = tmp
            permutation(v, start + 1, n)
            v[start] = v[i]
            v[i] = tmp

permutation(value, 0, len(value))

print (len(list_of_permutes))       # Number of permutations
list_of_permutes.sort()             # Sorts the list
print (list_of_permutes[999999])    # Prints the million'th permutation

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
