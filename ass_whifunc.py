

def factorial(n):
	
	if (n < 0):
		return "Can't calculate the factorial of negative numbers"

	elif n == 0 or n == 1:
		return 1

	else:
		result = 1
		while n > 1:
			result *= n
			n -= 1
			
		return result

try:
	num = int(input("Enter the number: "))

except ValueError:
	print("please enter a number")

y = factorial(num) 
print(f"The Factorial of {num} is {y}")

def even_num_sum(a):
	sum = 0
	while a > 0:
		if a % 2 == 0:
			sum += a
		a -= 1
	return sum		

try:
	num1 = int(input("Enter the number: "))

except ValueError:
	print("please enter a number")
x = even_num_sum(num1)
print(x)


