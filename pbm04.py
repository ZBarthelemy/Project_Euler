# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 09/02/16 

def main():
	n = 0
	for a in xrange(999,100,-1):
		for b in xrange(a, 100,-1):
			x = a * b
			if x > n:
				if isPalindrome(x):
						n = a * b
	print n

def isPalindrome(num):
	n = num
	rev = 0
	while (num > 0):
	  dig = num % 10
	  rev = rev * 10 + dig
	  num = num / 10
	if n == rev:
		return True
	else:
		return False

print main()