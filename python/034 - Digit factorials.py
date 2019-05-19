#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 0.891000032425 seconds.
#

# Description:
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# According to: http://mathworld.wolfram.com/Factorion.html
# Only 4 exists:
# 1 = 1!	          (1)
# 2 = 2!  	          (2)
# 145 = 1!+4!+5!          (3)
# 40585 = 4!+0!+5!+8!+5!  (4) 

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

def factorial(number):
    # Finds and returns the factorial sum of the number
    if number == 0:
        return int(1)
    tmp_sum = 0
    while number != 0:
        if tmp_sum == 0:
            tmp_sum = number
        else:
            tmp_sum *= number
        number -= 1
    return tmp_sum

def number_to_digits(number):
    # Takes the individual digits in a number and returns them as a list
    tmp_list = []
    str_num = str(number)
    for x in range(len(str_num)):
        tmp_list.append(int(str_num[x]))
    return tmp_list

final_sum = 0

for x in range(3, 50000): # Exclude 1 and 2, as written in the assignment
    digits = number_to_digits(x)
    tmp_num = 0
    for a in digits:
        tmp_num += factorial(a)
    if tmp_num == x:
        final_sum += x

print (final_sum)

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
