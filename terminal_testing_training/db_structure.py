class simpleUserDataStructure:
	def __init__(self, username='~', password='~', firstname='~', lastname='~'):
		self.username = username
		self.password = password
		self.firstname = firstname
		self.lastname = lastname

class userDataStructure:
	def __init__(self, id="", username="", password="", email="", firstname="", lastname="", dob="", gender="", height="", weight=""):
		self.id = id
		self.username = username
		self.password = password
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.dob = dob
		self.gender = gender
		self.height = height
		self.weight = weight

	def printUserDetails(self):
		print ("id : ", self.id)
		print ("username : ", self.username)
		print ("password : ", self.password)
		print ("email : ", self.email)
		print ("firstname : ", self.firstname)
		print ("lastname : ", self.lastname)
		print ("dob : ", self.dob)
		print ("gender : ", self.gender)
		print ("height : ", self.height)
		print ("weight : ", self.weight)

class foodDataStructure:
	def __init__(self, id=0, category="", description="", energy="0" , fat="0", saturates="0", carbohydrate="0", sugars="0", fibre="0", protein="0", salt="0"):
		self.id = id
		self.category = category
		self.description = description
		self.energy = energy
		self.fat = fat
		self.saturates = saturates
		self.carbohydrate = carbohydrate
		self.sugars = sugars
		self.fibre = fibre
		self.protein = protein
		self.salt = salt

	def printFoodDetails(self):
		print ("id : ", self.id)
		print ("category : ", self.category)
		print ("description : ", self.description)
		print ("energy : ", self.energy)
		print ("fat : ", self.fat)
		print ("saturates : ", self.saturates)
		print ("carbohydrate : ", self.carbohydrate)
		print ("sugars : ", self.sugars)
		print ("fibre : ", self.fibre)
		print ("protein : ", self.protein)
		print ("salt : ", self.salt)

	def printFoodDetailsInRow(self):
		print ("id : ", self.id , "  category : ", self.category , "  description : ", self.description)

class userFoodIntakeStructure:
	def __init__(self, id=0, userid = "0", datetime = "", foodid = "0", weight = "", foodcategory="", fooddescription="", energy="0" , fat="0", saturates="0", carbohydrate="0", sugars="0", fibre="0", protein="0", salt="0"):
		self.id = id
		self.userid = userid
		self.datetime = datetime
		self.foodid = foodid
		self.weight = weight
		self.foodcategory = foodcategory
		self.fooddescription = fooddescription
		self.energy = energy
		self.fat = fat
		self.saturates = saturates
		self.carbohydrate = carbohydrate
		self.sugars = sugars
		self.fibre = fibre
		self.protein = protein
		self.salt = salt
	def __str__(self):
		return str(self.id)

class userDailyIntakeStructure:
	def __init__(self, id=0, userid = "0", date = "", energy="0" , fat="0", saturates="0", carbohydrate="0", sugars="0", fibre="0", protein="0", salt="0"):
		self.id = id
		self.userid = userid
		self.date = date
		self.energy = energy
		self.fat = fat
		self.saturates = saturates
		self.carbohydrate = carbohydrate
		self.sugars = sugars
		self.fibre = fibre
		self.protein = protein
		self.salt = salt
	def __str__(self):
		return str(self.id)
