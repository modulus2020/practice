# More Classes and Class Inheritance


class Friend:
	def __init__(self, fname, nickname="Labalaba", sex="male", age=26):
		self.fname = fname
		self.nickname = nickname
		self.sex = sex
		self.age = age

	def character(self):
		print(self.fname +self.nickname +" is ", self.age, " years old and he is a " +self.sex)

mike = Friend("Mike ")
royal = Friend("Royal ")

mike.character()
royal.character()
print(royal.sex)
print(mike.nickname)

class Bigboys(Friend):
	def __init__(self, fname, nickname="Big boys", sex="male", age="35"):
		self.fname = fname
		self.nickname = nickname
		self.sex = sex
		self.age = age

mike = Bigboys("Mike ")
royal = Bigboys("Royal ")
royal.character()




