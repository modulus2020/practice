import random

number = random.randint(1, 5)
def guesss():
	while True:
		guess = int(input("Enter your guess: "))

		if guess == number:
			print("You won")
			break
		elif guess > number:
			print("Your guess is too high")
		else:
			print("Your guess is too low")

guesss()