#   Project Euler Solutions 
#   Edward Barthelemy
#   A good warmup back into it
#   Finished 09/01/16 

def main():
	count = 0
	x = 1
	y = 2
	while(x <= 4000000):
		if x % 2  == 0:
			count += x
		x, y = y, x + y
	return str(count)

print main()