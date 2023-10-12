import sys

"""
try:
	raise Exception("sky", "rock")
except Exception as inst:
	print(inst)
	print(inst.args)
	print(type(inst))
	
	x, y = inst.args
	print("x = ", x)
	print("y = ", y)

try:
	f = open("dels.txt")
	l = f.readline()
	g = int(l.strip())

except OSError as err:
	print("The Os experienced an error", err)
except ValueError:
	print("Wrong value entered")
except Exception as err:
	print(f"Unexpected error {err}, {type(err)}")



try:
	f = open("dict.py")
	
	print("has", len(f.readlines()), "lines")
	f.close

except OSError:
	print("error occurred, Cannot open dels")


def this_one():
	x = 1/0

try:
	this_one()
except ZeroDivisionError as err:
	print("Runtime error:", err)
else:
	print("has", len(f.readlines()), "lines")
	f.close

def flew():
	raise ConnectionError
	
try:
	flew()
except ConnectionError as exc:
	raise RuntimeError("Having an issue") from exc
"""

try:
	f = open("database.txt")
except OSError:
	raise RuntimeError("Nothing to open") from None

