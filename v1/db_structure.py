class userDataStructure:
	def __init__(self, id, username, password, email, firstname, lastname, dob, gender, height, weight):
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