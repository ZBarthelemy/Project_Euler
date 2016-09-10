# Project Euler Solutions 
# Edward Barthelemy
# PBM 05
# Finished 09/10/16 
# 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def lcm(x, y):
        return (x * y) // gcd(x, y)

def main():
	n = 1
	for i in xrange(1,21):
		n = lcm(n , i)
	print n

main()