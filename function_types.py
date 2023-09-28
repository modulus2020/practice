# The different types of python functions are:

# Empty functions
def my_name():
	pass

# Functions with a single argument
def my_name(name):
	pass

# Functions with more than one argument
def my_name(a, b):
	pass

# Functions with arbitrary arguments
def my_name(*name):
	pass

# Functions with keyword arguments
def my_name(fname="hector", lname="Troy"):
	pass

# Functions with arbitrary keyword arguments
def my_name(**kword):
	pass

# Functions with default parameter
def my_name(country = "Nigeria"):
	pass


# Lambda Functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))

z = lambda a, b, c : b * (a + c) 
print(z(5, 6, 2))

# The power of lambda function is using it as an annonymous function in other functions
def myfunc(n):
  return lambda a : a * n

my_fan = myfunc(4)
print(my_fan(11))

# Function recursion

def recursion(n):
	if (n > 0):
		result = n * recursion(n - 1)
	elif n == 0 or n == 1:
		result = 1
	else:
		result = 0
	return result
y = recursion(0)
print(y)