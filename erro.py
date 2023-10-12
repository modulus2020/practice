
class CustomError(Exception):
	def __init__(self, message):
		super().__init__(message)

def divide(x, y):
	if y == 0:
		raise CustomError("cannot divide by zero")
	else:
		return x/y

try:
	result = divide(12, 0)
except CustomError as err:
	print(f"something went wrong: {err}")
else:
	print("result = ", result)

class B(Exception):
	pass


try:
	raise B
except B:
	print("Nothing here")
		