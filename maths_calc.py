# Accept user input for three data, num1, operator, num2 example 5 + 4 
num1, operator, num2 = input("Enter a mathematical operation: ").split()

# Convert the num1 and num2 into floats or integers
num1 = int(num1)
num2 = int(num2)

""" Operators
1. >
2. <
3. == example x == y 
4. Assignment operator =  example x = y
5. >= 
6. <=
7. !=

www.w3schools.com

"""

if (operator == "+"):
	print("{} + {} = {}".format(num1, num2, num1 + num2))

elif operator == "-":
	print("{} - {} = {}".format(num1, num2, num1 - num2))

elif operator == "*":
	print("{} x {} = {}".format(num1, num2, num1 * num2))

elif operator == "/":
	print("{} / {} = {}".format(num1, num2, num1/num2))

elif operator == "%":
	print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
	print("Your operator should either be +, -, *, / or %")


