#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-25
# Computation time: 0.0160000324249 seconds.
#

# Description:
# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
# 3
# 7 5
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt,
# a 15K text file containing a triangle with one-hundred rows.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The numbers
numbers = []

# Opens the log file and read the data to a list
logfile = open('067 - triangle.txt', 'r')

for n in range(100):
    tmp_str = logfile.readline()
    #tmp_str = tmp_str.replace( ' ', ', ' )
    #print type(eval(tmp_str))
    #print tmp_str
    tmp_list = []
    for x in range(0, len(tmp_str), 3):
        if tmp_str[x] == '0':
            tmp_list.append(int(tmp_str[x+1]))
        else:
            tmp_list.append(int(tmp_str[x:x+2]))
    numbers.append(tmp_list)

logfile.close()

# Algorithm:
# Look at one "sub-triangle" at the bottom such as
#  
#   63
# 04  62
#
# Simply replace 63 with the sum of 63 and the largest
# of its "children" in this case 62. That is we get
#
#   125
# 04   62
#
# Do this for the "sub-triangles" on the last two rows.
# Next move up one row and rinse and repeat.
# When we reach the top we get the result in the top-most cell.

for n in range(len(numbers) - 2, -1, -1):
    for x in range(len(numbers[n])):
        #print numbers[n][x], max(numbers[n+1][x], numbers[n+1][x+1])
        numbers[n][x] = numbers[n][x] + max(numbers[n+1][x], numbers[n+1][x+1])

# Prints the number
print (numbers[0][0])    

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
