#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-27
# Computation time: 5.875 seconds.
#

# Description:
# The Fibonacci sequence is defined by the recurrence relation:
#
#    F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.
#
# It turns out that F(541), which contains 113 digits,
# is the first Fibonacci number for which the last nine digits are 1-9 pandigital
# (contain all the digits 1 to 9, but not necessarily in order). And F(2749),
# which contains 575 digits, is the first Fibonacci number for
# which the first nine digits are 1-9 pandigital.
#
# Given that F(k) is the first Fibonacci number for which the
# first nine digits AND the last nine digits are 1-9 pandigital, find k.

# Imports
import math

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

numbers = 2
fibonacci = [1,1]

def fibonacci_next(n2, n1):
    # Returns the next number in the fibonacci sequence
    next = n2 + n1
    return next % 10 ** 9

def str_to_digits(string):
    # Takes a string and returns the individual digits as a list
    string = str(string)
    tmp_list = []
    for x in range(len(string)):
        tmp_list.append(int(string[x]))
    tmp_list.sort()
    return tmp_list

def is_pandigital(tmp):
    if str_to_digits(tmp) == [1,2,3,4,5,6,7,8,9]:
        return True
    return False

def top_digits(num):
# http://blog.dreamshire.com/2009/06/04/project-euler-problem-104-solution/
# top = num * log10(phi)          + log10(1/sqrt(5))
  top = num * 0.20898764024997873 - 0.34948500216800940
  top = int((pow(10, top - int(top) + 8)))
  return top

while True:
    fibonacci.append(fibonacci_next(fibonacci[-2],fibonacci[-1]))
    numbers += 1
    fibonacci = fibonacci[-3:]
    #print len(fibonacci), len(str(fibonacci[-1]))
    try:
        first = str(fibonacci[-1])[:9]
        if is_pandigital(first):
            #print numbers, first, len(str(fibonacci[-1]))
            last = top_digits(numbers) #str(fibonacci[-1])[-9:]
            if is_pandigital(last):
                print (numbers)
                break
    except Exception as e:
        print (e)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
