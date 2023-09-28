from decimal import Decimal as D



def add(a, b):

	"""
	Given two integers, return the sum of them
	
	:param a: int
	:param b: int
	:return: int

	>>> add(2, 3)
	5

	>>> add(0, 0)
	2
	"""
	return a + b

if __name__ == "__main__":
	import doctest
	doctest.testmod()


# Write a python script that collects a word and returns the number of vowels in it>
# Use the python test module to test your codes...



sum = 0
sum += D("0.4")
sum += D("0.4")
sum += D("0.4")
sum -= D("1.2")

print(sum)

print("sum = ", 0.4 + 0.4 +  0.4 - 1.2)