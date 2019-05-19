#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-31
# Computation time: 37.1720001698 seconds.
#

# Description:
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on.
# In this way, we note the following:
#
#    * d_(2)d_(3)d_(4)=406 is divisible by 2
#    * d_(3)d_(4)d_(5)=063 is divisible by 3
#    * d_(4)d_(5)d_(6)=635 is divisible by 5
#    * d_(5)d_(6)d_(7)=357 is divisible by 7
#    * d_(6)d_(7)d_(8)=572 is divisible by 11
#    * d_(7)d_(8)d_(9)=728 is divisible by 13
#    * d_(8)d_(9)d_(10)=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def permutation(v, start, n):
    # Permutation implementation
    # v = list, start = 0, n = len(v)
    if start == n-1:
        #print v
        string = ''
        for a in v:
            string += str(a)
        global list_of_permutes
        if str(string)[5] == '5':
            list_of_permutes.append(int(string))
    else:
        for i in range(start, n):
            tmp = v[i]
            v[i] = v[start] 
            v[start] = tmp
            permutation(v, start + 1, n)
            v[start] = v[i]
            v[i] = tmp

def ispandigital(number):
    # Returns the truth of the number is pandigital
    pandigital = [0,1,2,3,4,5,6,7,8,9]
    tmp_list = []
    string = str(number)
    for s in string:
        tmp_list.append(int(s))
    tmp_list.sort()
    if tmp_list == pandigital[:len(tmp_list)]:
        return True
    return False

init = [0,1,2,3,4,5,6,7,8,9]
list_of_permutes = []
the_list = []

# Get all the permutations of the init, as those are the only we need checking
permutation(init, 0, len(init))

# Seeing as int(str(x)[3:6]) % 5, we know that the 6'th digit must be 5 or 0,
# and if it is 0, then int(str(x)[5:8]) % 11 must be 11,22,33,44, etc.. which is not possible;
# Thus we know the 6'th digit must be 5.. and we can safely delete the rest.
#for x in list_of_permutes:
#    if not str(x)[5] == '5': #0...5 = 6
#        list_of_permutes.remove(x)

# Run through the rest, checking if they follow the pattern
for x in list_of_permutes:
    if int(str(x)[1:4]) % 2 == 0:
        if int(str(x)[2:5]) % 3 == 0:
            if int(str(x)[3:6]) % 5 == 0:
                if int(str(x)[4:7]) % 7 == 0:
                    if int(str(x)[5:8]) % 11 == 0:
                        if int(str(x)[6:9]) % 13 == 0:
                            if int(str(x)[7:10]) % 17 == 0:
                                if ispandigital(x):
                                    the_list.append(x)
                                    print (x)

print (sum(the_list))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
