

class Person():
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname
	
	def __str__(self):
		return f"{self.lname} {self.fname}"

	def hello(self):
		print("Hello ", self.fname +" you are welcome")

	
	
pp = Person("Emmanuel ", "Amadi")
print(pp)	
pp.hello()




class Calculator():
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def summ(self):
		return self.a + self.b

	def subtract(self):
		return self.a - self.b

	def multiply(self):
		return self.a * self.b

	def divide(self):
		if self.b == 0:
			return "cannot divide by zero"
		else:
			return self.a/self.b

pa = Calculator(4, 10)

print(pa.summ())
print(pa.multiply())
print(pa.subtract())
print(pa.divide())













































 