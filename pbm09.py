# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 09/12/16
# A Pythagorean triplet is a set of three natural numbers, a < b < c for which,
# a^2 + b^2 = c^2 i.e. 3^2+4^2 = 9 + 16 = 25 = 5^2
# There exist exactly one Pythagorean triplet for which a + b + c = 1000. Find the product a b c

def is_pythagorean_triple(x, y, z):
    return x ** 2 + y ** 2 == z ** 2

for x in range(1, 1000):
    for y in range(x, 1000 - x):
        z = 1000 - x - y
        if z < y:
            break
        if is_pythagorean_triple(x, y, z):
            print(x, y, z)
            print("Product: {}".format(x * y * z))
            exit(0)
