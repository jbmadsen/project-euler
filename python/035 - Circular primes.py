#
# Author:           Jacob B. Madsen
# Email:            jacob@jbmadsen.com
# Date:             2009-07-26
# Computation time: 12.1410000324 seconds.
#

# Description:
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

# Imports time and start counting
import time
start = time.time()
print ("Starting...")

# The list of circular primes
list_of_circular_primes = []

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

list_of_primes = generate_primes(1000000)

# Removes all elements who does not only constain ['1','3','7','9']
# With exception of the single digit primes
for x in list_of_primes[3:]:
    for a in str(x):
        if ['1','3','7','9'].count(a) == 0:
            list_of_primes.remove(x)
            break      

# Circle the number
def circle_prime(number, rotate):
    tmp_str = str(number)
    for _ in range(rotate):
        tmp_str = tmp_str[len(tmp_str)-1] + tmp_str[0:len(tmp_str)-1]
        if not int(tmp_str) < 10:
            if ['1','3','7','9'].count(tmp_str[len(tmp_str)-1]) == 0:
                return False
        if not int(tmp_str) in list_of_primes:
            return False
    return True

# Main
for x in list_of_primes:
    # Break if above one million
    if x > 1000000:
        break
    # Add to the final list if circular
    if circle_prime(x,len(str(x))):
        list_of_circular_primes.append(x)

#Prints the result
print (len(list_of_circular_primes))

# Prints the time to complete
print ("Done in " + str(time.time()-start) + " seconds.")
