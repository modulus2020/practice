# Python dictionaries have keys and values and are array kind of data types with their 
# items enclosed in curly braces  
"""
my_dictionary = {'username': 'samuel', 'Nickname' : 'Pablo', 'followers' : 4000}

my_dictionary["project"] = "catparty"
print(my_dictionary)
"""

username = {"sammy" : "Black", "Dupe" : "white"}
while True:

	print("Enter name: ")

	name = input()

	if name in username:
		print(username[name] +" is the color of ", name)
		break
	else:
		print(name, " not found, please update the record")

		user = input("Enter the new name : ")
	
		username[name] = user

		print("Record updated")

		print("would you like to see the new update?")

		res = input(" Enter y or n: ")
		if res == "y":
			print(username)
		else:
			print("Done")
	
	
	