class CustomError(Exception):
	def __init__(self, message):
		super().__init__(message)

def divide(x, y):
	if y == 0:
		raise CustomError("Cannot divide by zero")
	else:
		return x/y

class NameError2(NameError):
	def __init__(self, message):
		super().__init__(message)


try:
	d = divide(12, 0)
except CustomError as err:
	print("Something went wrong", err)
else:
	print("result = ", result)







