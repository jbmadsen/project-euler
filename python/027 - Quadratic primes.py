#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-28
# Computation time: 45.5 seconds.
#

# Description:
# Euler published the remarkable quadratic formula:
#
#   n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
# However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41� + 41 + 41 is clearly divisible by 41.
#
# Using computers, the incredible formula  n� - 79n + 1601 was discovered,
# which produces 80 primes for the consecutive values n = 0 to 79.
# The product of the coefficients, -79 and 1601, is -126479.
#
# Considering quadratics of the form:
#
#    n^2 + an + b, where |a| < 1000 and |b| < 1000
#
#    where |n| is the modulus/absolute value of n
#    e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# Imports decimal, to enable custom decimal points
import decimal

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# Function to generate the primes
def generate_primes(n):
    # Sieve Of Eratosthenes
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
    return [i for i in range(2, len(prime)) if prime[i] == True]

list_of_primes = generate_primes(1000)

print (len(list_of_primes))
list_of_primes = list_of_primes[:1000]#[:len(list_of_primes)/40]
print (len(list_of_primes))
print (list_of_primes[-1])
print ("-" * 40)

numbers = [0,0,0] # a, b, len

for a in range(-999,999,2):
    #print a
    for b in range(-999,999,2):
        length = 0
        n = 1
        while (n**2 + a*n + b) in list_of_primes:
            n += 1
        if n > numbers[2]:
            numbers[0] = a
            numbers[1] = b
            numbers[2] = n
            print (numbers)

print (numbers[0]*numbers[1])

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
