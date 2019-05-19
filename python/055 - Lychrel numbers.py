#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-08-01
# Computation time: 0.639999866486 seconds.
#

# Description:
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# 
# Not all numbers produce palindromes so quickly. For example,
#
#       349 + 943 = 1292,
#       1292 + 2921 = 4213
#       4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196,
# never produce a palindrome. A number that never forms a palindrome through the
# reverse and add process is called a Lychrel number.
# Due to the theoretical nature of these numbers, and for the purpose of this problem,
# we shall assume that a number is Lychrel until proven otherwise.
# In addition you are given that for every number below ten-thousand, it will either
# (i) become a palindrome in less than fifty iterations, or,
# (ii) no one, with all the computing power that exists,
# has managed so far to map it to a palindrome.
# In fact, 10677 is the first number to be shown to require
# over fifty iterations before producing a palindrome: 4668731596684224866951378664
# (53 iterations, 28-digits).
# 
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
# the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?

# Imports time and start counting
import time
start = time.time()
print ("Starting...") 

def reverse_int(number):
    # Function that returns the reverse of an integer
    temp_str = str(number)          # convert the int to a string
    rev_str = reversed(temp_str)    # reverse the string (returns an object)
    rev_list = list(rev_str)        # puts the reversed object in a list
    rev_str = "".join(rev_list)     # joins the elements in the list to a string
    temp_int = int(rev_str)         # convert the string back to an int
    return temp_int                 # returns the now reversed string

def ispalindromic(num):
    # Checks if a number is palindromic, returns bool
    tmp_str = str(num)
    tmp_rev = reversed(tmp_str)
    tmp_list = list(tmp_rev)
    tmp_rev = "".join(tmp_list)
    if tmp_str == tmp_rev:
        return True
    return False

lychrel = 0

for n in range(1,10000):
    n += reverse_int(n)
    if ispalindromic(n):
        pass
    else:
        x = 1
        while x < 50:
            n += reverse_int(n)
            if ispalindromic(n):
                break
            else:
                x += 1
        if x >= 50:
            lychrel += 1

print (lychrel)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
