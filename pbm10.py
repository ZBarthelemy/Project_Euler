# Summation of primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

foo = 0

for n in range(1,2000001):
	if is_prime(n): foo += n
print foo
