# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 09/01/16 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Fundamental thorem of arithmetic states  every integer n > 1 has a unique factorization as a product of prime numbers.
# The number might not be unique by we keep facorting out primes until we find the lowest one, the first must be the largest

n = 600851475143
i = 2

while i * i < n:
	while n % i == 0:
		n = n / i
	i = i + 1

print n