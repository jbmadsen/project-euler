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