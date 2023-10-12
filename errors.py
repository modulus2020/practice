

import sys
"""
try:

	f = open("dic.py")

except OSError as rock:
	print("File too hot", rock)
except NameError as kak:
	print("Sorry, you must define your variables", kak)
except ValueError:
	print("there is a value error")

else:
	h = f.readlines()
	print("there are ", len(h), "lines")

finally:
	print("Thank you for using my App")


Exception Handling
1. using the try and except blocks
2. Using the try, except and Else blocks
3. Using the try, except, else and Finally blocks

4. Raising exceptions

try:
	raise TalkingError("Hi there")
except TalkingError:
	print("Sorry")
"""

for line in open("dict.py"):
	print(line, end="")
	

with open("dic.py") as f:
	for line in f:
		print(line, end="")