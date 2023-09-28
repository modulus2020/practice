import random

# To find the sum of the even numbers in a range of numbers
# User input is required
# The upper limit of the range is accepted as user input
# while loop and use a function to organize the logic

"""
def sum(n):
	total = 0
	start_num = 1
	while start_num <= n:
		if start_num % 2 == 0:
			total += start_num
		start_num += 1
	return total

try:
	num = int(input("Enter number : "))

except ValueError:
	print("only integers are required")
except NameError:
	print("Only integers are required")

y = sum(num)
print(f"The sum of the even numbers from 1 to {num} is {y}")	


def factorial(n):
	total = 1
	while n > 1:
		total *= n
		n -= 1
	return total


try:
	num1 = int(input("Enter the number for a factorial : "))

except ValueError:
	print("only integers are required")
except NameError:
	print("Only integers are required")

x = factorial(num1)
print(f"The factorial of {num1} is {x}")


# The Guessing Game

number = random.randint(1, 100)

def guessing():
	while True:
		user = int(input("Guess the number between 1 and 100 : "))
		if user < number:
			print("Too low")
		elif user > number:
			print("Too High")
		else:
			print("Congratulations, you've guessed the correct number")
			break

guessing()


0, 1, 2, 3, 8
 "madam"


# madam, i'm adam
# was it a cat i saw
# boob

# def palindrom_test(word):
#	word_cleaner = " ".join(word.split()).lower()
#	length_word = len(word_cleaner)
	i = 0
	while i < length // 2:
		if word_cleaner[i] != word_cleaner[length - i - 1]:
			return False
		i += 1
	return True




# Functions

def my_function():
	print("This is my Function")

my_function()

def my_function2():
	pass

def my_function2(name):
	print("My name is " +name)

my_function2("Jackson")



def my_function3(lname, fname):
	print("My father is " +lname + " " + "while i am " +fname)

my_function3("Jackson", "Joshua")


def sumn(a, b):
	return a + b

print(sumn(4, 5))
print(sumn("Hi ", "There"))

def my_func(*name):
	print("Here is " +name[3])

my_func("Jack", "Josh", "Sam", "Royal", "Miracle")


def my_funct(kid1, kid2, kid3):
	print("This is " +kid1)

my_funct(kid1 = "Joy", kid2 = "Kate", kid3 = "Mary") 

def my_func2(**kid):


lambda 
	


def palindrom_test(word):
	word_cleaner = " ".join(word.split()).lower()
	length_word = len(word_cleaner)
	i = 0
	while i < length_word // 2:
		if word_cleaner[i] != word_cleaner[length_word - i - 1]:
			return False
		i += 1
	return True


word1 = input("Enter the word to test: "))

y = palindrom_test(word1)
print(y)
"""


def vowel_checker(addd):
	i = 0
	if "aeiou" in wordd:
		for vowel in wordd:
			print(vowel)
		i += 1
		return True
	
	else:
		return False

wordd = str(input("Enter the word: "))
ab = vowel_checker(wordd)
print(ab)



		
	

