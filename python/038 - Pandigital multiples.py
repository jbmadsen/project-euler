#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-30
# Computation time: 0.18700003624 seconds.
#

# Description:
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#    192 * 1 = 192
#    192 * 2 = 384
#    192 * 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

pandigital = [1,2,3,4,5,6,7,8,9]

def to_list(string):
    # Takes a string and returns a list of its content
    tmp_list = []
    for a in string:
        tmp_list.append(int(a))
    return tmp_list

number = 1 # Primary number
n = 1 # Number multiplied to number
string = '' # String containing the concatenated products
final = 0 # Final value to print

while number < 10000:
    n = 1
    string = ''
    while len(string) < 9:
        string += str(number * n)
        n += 1
    tmp = to_list(string)
    tmp.sort()
    if tmp == pandigital:
        print (string, "(", number, ")")
        if int(string) > final:
            final = int(string)
    number += 1

print ("Highest number:", final)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
