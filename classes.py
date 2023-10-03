import math

# We are to develop a calcuator

# Include user input  

# User input should be integers but casted to floats

# print("please enter the operation you want to perform")
# print("For addition enter add")
# print("For subtraction enter subtract")
# print("For multiplication enter multiply")
# print("For division enter divide")
# print("For modulo enter modulo")
# print("Enter exit if you want to quit")





class Calculator:

	def __init__(self):
		self.num1 = 0
		self.num2 = 0

	def set_numbers(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def addition(self):
		return self.num1 + self.num2	

	def subtract(self):
		return self.num1 - self.num2	


	def multiply(self):
		return self.num1 * self.num2	

	def modulo(self):
		return self.num1 % self.num2	

	
	def divide(self):
		if self.num2 == 0:
			return "cannot divide by zero"
		else:
			return self.num1/self.num2

calculator = Calculator()

while True:
	print("please enter the operation you want to perform")
	print("For addition enter add")
	print("For subtraction enter subtract")
	print("For multiplication enter multiply")
	print("For division enter divide")
	print("For modulo enter modulo")
	print("Enter exit if you want to quit")

	user_input = input(":  ")

	if user_input == "exit":
		break

	elif user_input in ("add", "subtract", "multiply", "divide", "modulo"):
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))

		calculator.set_numbers(num1, num2)
	
		if user_input == "add":
			result = calculator.addition()
		elif user_input == "subtract":
			result = calculator.subtract()
		elif user_input == "multiply":
			result = calculator.multiply()
		elif user_input == "divide":
			result = calculator.divide()
		elif user_input == "modulo":
			result = calculator.modulo()

		print("Result: ", result)
		print()

	else:
		print("Invalid operation")



# Add other operations like

# sine, cosine, log, factorial, square root and square










































 