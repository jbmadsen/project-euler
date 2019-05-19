#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 0.0160000324249 seconds.
#

# Description:
# The square root of 2 can be written as an infinite continued fraction.
#
#       ( LOOK AT https://projecteuler.net/problem=65 )
#
# The infinite continued fraction can be written, v2 = [1;(2)], (2) indicates
# that 2 repeats ad infinitum. In a similar way, v23 = [4;(1,3,1,8)].
#
# It turns out that the sequence of partial values of continued fractions for square roots
# provide the best rational approximations. Let us consider the convergents for v2:
#
#       ( LOOK AT https://projecteuler.net/problem=65 )
#
# Hence the sequence of the first ten convergents for v2 are:
# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
#
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#
# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#
# The sum of digits in the numerator of the 10^(th) convergent is 1 + 4 + 5 + 7 = 17.
# 
# Find the sum of digits in the numerator of the 100^(th) convergent
# of the continued fraction for e.

# Imports time and start counting
import time
start = time.time()
print ("Starting...") 

# With assistance from:
# http://blog.dreamshire.com/2009/04/10/project-euler-problem-65-solution/
number = 2           # The beginning number in the sequence
total_div = 1        # The total value for division
iterations = 100     # Max number of iterations

while iterations > 0:
    divisor = 1
    if iterations % 3 == 0:
        # Every third time, the dividor needs to be double of the (iteratoer/3)
        divisor = 2 * iterations // 3
    tmp_number = number
    number = total_div
    total_div = divisor * total_div + tmp_number # New total of the division so far
    iterations -= 1

print ("Sum of int(d):", sum(int(x) for x in str(total_div)))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
