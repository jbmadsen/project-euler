#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-27
# Computation time: 0.0469999313354 seconds.
#

# Description:
# The n^(th) term of the sequence of triangle numbers is given by, t(n) = �n(n+1);
# so the first ten triangle numbers are:
#
#       1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t_(10).
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
# nearly two-thousand common English words, how many are triangle words?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

alphabet = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
triangle_numbers = []
numbers = 0

# Imports the data to a list
logfile = open('words.txt', 'r')
words = eval(logfile.readline())
words = list(words)
logfile.close()

def to_number(string):
    # Converts the string to a number based on the alphabet
    number = 0
    string = string.lower()
    for x in range(len(string)):
        number += alphabet.index(string[x])
    return number

# Generate the list of triangle numbers (2000 should be enough)
for x in range(1,200):
    triangle_numbers.append(int(0.5 * x * (x + 1)))

for element in words:
    if to_number(element) in triangle_numbers:
        numbers += 1

print (numbers)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
