# Accept input of two numbers and store in variables
num1, num2 = input("Enter two numbers: ").split()

num1 = int(num1)
num2 = int(num2)

# Add the two numbers and store in a variable called sum
sum = num1 + num2

# Subtract the two numbers and store in a variable called difference
difference = num1 - num2

# Multiply the two numbers and store in a variable called product
product = num1 * num2

# Divide the two numbers and store in a variable called quotient
quotient = num1 / num2

# Find the remainder and store in a variable called remainder
remainder = num1 % num2

# print out your results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))

