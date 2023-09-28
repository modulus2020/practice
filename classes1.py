import math
from classes import Friends


def vowel_count(word):
	"""
	Given a word, return the number of vowels in it

	:param word: str
	:return: int

	>>> vowel_count("manila")
	3

	>>> vowel_count("count")
	2
	"""
	vowels = 0
	for letters in word:
		if letters in "aeiou":
			vowels += 1
	return vowels

if __name__ == "__main__":
	import doctest
	doctest.testmod()


class Calculator:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def add(self):
		return self.x + self.y

	def sub(self):
		return self.x - self.y

	def multiply(self):
		return self.x * self.y
  
	def division(self):
		return self.x / self.y

	def square_root(self):
		return sqrt(self.x)

	def factorial(self):
		return factorial(self.x)

	def square(self):
		return self.x * self.x

	def sine_degrees(self):
		return math.sin(self.x)