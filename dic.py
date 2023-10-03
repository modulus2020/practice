
names = {"Tom" : "Black", "Sam" : "white", "Angel" : "Fair"}

"""
print(names["Tom"])

print(names)

# key and value methods

print(names.keys())

print(names.values())

for key, value in names.items():
	print(key, " is the key for the value ", value)


names["Sam"] = "Green"
print(names)

"""
for x in range(2):

	username = input("Enter your name: ")

	if username in names:
		print(username, " is found and your color is ", names[username])

	else:
		print("sorry, your name is not in the database, ")
		print("would you want to update it?")

		update = input("Enter y or n :")
		
		if update == "y":
			names[username] = "Green"
		else:
			print("Operation Successful") 
	 
