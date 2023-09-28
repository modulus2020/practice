"""

x = lambda a : a + 10
print(x(6))

def summ(a, b):
	return a + b
print(summ(5, 10))

y = lambda a, b : a + b
print(y(5, 15))

z = lambda a, b, c : b * (a + b + c)
print(z(1, 2, 3))






def complex(b):
	return lambda a : a * b

p = complex(5)
print(p(10))

def summm(a, b):
	return lambda c, d : c + d + a + b

c = summm(1, 3)
print(c(2, 3))

"""


# Classes

class Dog():
	x2 = 10   # Is a class variable

p = Dog.x2   # This is an instance of the class person
print(p)




class Person():
	def __init__(self, name, age, complexion):
		self.name = name
		self.age = age
		self.complexion = complexion


p1 = Person("Josh", 35, "Fair")
print(p1.age)
print(p1.name)
print(p1.complexion)








































