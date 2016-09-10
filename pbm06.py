# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 09/10/16
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 55^2 = 3025
# The difference between the sum of the squares and square of the sum of the first 10 terms is 3025-386 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquare(i):
	count = 0
	for n in range(i, 0, -1):
		count += n**2
	return (count)

def squareOfSums(i):
	count = 0
	for n in range(i, 0, -1):
		count += n
	return (count**2)

x,y = sumOfSquare(100), squareOfSums(100)
print str(y-x)