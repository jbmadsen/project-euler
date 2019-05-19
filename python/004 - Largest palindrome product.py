#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-23
# Computation time: 0.0780000686646 seconds.
#

# Description:
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Our palindrome number
palindrome = 0

def reverse_int(number):
    # Function that returns the reverse of an integer
    temp_str = str(number)          # convert the int to a string
    rev_str = reversed(temp_str)    # reverse the string (returns an object)
    rev_list = list(rev_str)        # puts the reversed object in a list
    rev_str = "".join(rev_list)     # joins the elements in the list to a string
    temp_int = int(rev_str)         # convert the string back to an int
    return temp_int                 # returns the now reversed string

# Finds the palindromes (highest to lowest)
for x in range(999,900,-1):
    for y in range(999,900,-1):
        rev_palindrome = reverse_int(x * y)
        if rev_palindrome == x * y:
            if (x * y) > palindrome:
                palindrome = (x * y)

# Prints the list
print ("Largest 3x3 digit palindrome number: " + str(palindrome))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
