# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 11/15/16

# The following iterative sequence is defined for the set of positive integers: ]
# n->n/2 if n is even or n->3n+2 if n is odd
# Using the rule above and starting with 13 we generate the following sequence 
# : 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 finishing at 1) contains 10 terms. 
# Although it has not yet been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# WHICH starting number, under one million, produces the longest chain?

# There exist more efficient soltions to do this but 1 million is not such a big number for this type of sequence.
from array import array

def CollatzPath(n):
	count = 0 
	while n > 1:
		count += 1
		if n % 2  == 0:
			n /= 2
		else:
			n = n*3 + 1
	return count

large = [1] * 2

for n in range(2,1000001):
	length = CollatzPath(n)
	if length > large[0]:
		large[0] = length
		large[1] = n

print "largest path for n < 1mil is " + str(large[0]) + " length with number " + str(large[1])