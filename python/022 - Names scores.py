#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-27
# Computation time: 0.421999931335 seconds.
#

# Description:
# Using names.txt (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 � 53 = 49714.
#
# What is the total of all the name scores in the file?

# Imports the math module
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The alphabet
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# The list of the names
names = []

# Opens the log file and read the data to a list
logfile = open('022 - names.txt', 'r')
names = eval(logfile.readline())
logfile.close()

# Sort the names alphabetically
names.sort()

def get_value_of_name(num):
    # Finds the name at the given index and calculates the value of the name
    # Then returns it as an int
    tmp_name = names[num]
    tmp_name = tmp_name.lower()
    #print tmp_name
    value = 0
    for x in range(len(tmp_name)):
        for n in alpha:
            #print n, tmp_name[x]
            if tmp_name[x] == n:
                value += alpha.index(n) + 1
    value *= (num + 1)
    return value

# Value for print
value = 0

# Loop through all names, gets their values
for x in range(len(names)):
    value += get_value_of_name(x)

# Prints the combined value
print (value)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
