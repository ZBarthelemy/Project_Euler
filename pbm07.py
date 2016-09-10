# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 09/02/16
# The first 6 prime numbers are 2,3,5,7,11,13.  Find the 10001 prime number

#discovered the all loop, avoiding iteration with invalid factor
#http://codereview.stackexchange.com/questions/102507/finding-the-10001st-prime states the sieve of eratosthenes
#much much faster.  Commented out this solution

def primes(n):
    primes = [2]
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    return str(primes[-1])

print primes(10001)


# def primes_sieve(n):
#     p_n = int(2 * n * math.log(n))       # over-estimate p_n
#     sieve = [True] * p_n                 # everything is prime to start
#     count = 0

# for i in range(2, p_n):
#     if sieve[i]:                       # still prime?
#         count += 1                     # count it!
#         if count == n:                 # done!
#             return i
#         for j in range(2*i, p_n, i):   # cross off all multiples of i
#             sieve[j] = False