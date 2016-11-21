# Project Euler Solutions 
# Edward Barthelemy
# A good warmup back into it
# Finished 11/15/16
# pbm 17 Project Euler

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# It is best ot use switch statements to catch errors, it is likely slower than using arrays in terms of lookup time but this is computing efficiency not a constraint in this problem.

def singleDigitLength(n):
	if n == 0: return 0
	elif n == 1 or n == 2 or n == 6:
		return 3
	elif n == 4 or n == 5 or n == 9 :
		return 4
	elif n == 3 or n == 7 or n == 8:
		return 5

def teen(n):
	if n == 11 or n == 12: return 6
	elif n == 16 or n == 15: return 7
	elif n ==13 or n == 14 or n == 18 or n == 19: return 8
	elif n == 17: return 9
	elif n == 10: return 3
	else: return 0

def decaDigitLength(n):
	if n == 0: return 0
	if n == 1: return 3
	if n == 4 or n == 5 or n == 6:
		return 5
	if n == 2 or n == 3 or n == 8 or n == 9:
		return 6
	if n == 7:
		return 7

def hundred():
	return 7

def thousand():
	return 8

foo = 0

for i in range(1,1001):
	if i < 10:
		foo += singleDigitLength(i)
	elif i < 20:
		foo += teen(i)
	elif i < 100:
		if i % 10 != 0:
			deca = i / 10
			single = i % 10
			foo += decaDigitLength(deca)+singleDigitLength(single)
		else:
			deca = i / 10
			foo += decaDigitLength(deca)
	elif i < 1000:
		substring = str(i)
		teens = int(substring[1]+""+substring[2])
		hecto = int(substring[0])
		deca = int(substring[1])
		single = int(substring[2])

		if deca == 0 and single != 0:
			foo += singleDigitLength(hecto)+hundred()+3+singleDigitLength(single)
		elif deca == 1:
			foo += singleDigitLength(hecto)+hundred()+3+teen(teens)
		elif deca > 1 and single == 0:
			foo += singleDigitLength(hecto)+hundred()+3+decaDigitLength(deca)
		elif deca > 1 and single != 0:
			foo += singleDigitLength(hecto)+hundred()+3+decaDigitLength(deca)+singleDigitLength(single)
	elif i == 1000: foo += thousand()

print foo