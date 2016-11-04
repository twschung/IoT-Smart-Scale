import pymysql.cursors

def connectToServer():
	connection = pymysql.connect(host='42.2.205.124',user='admin',password='abcd1234',db='smartscale',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	return connection

def food_register(inputFood):
	try:
		serverConnection = connectToServer()
		cursor = serverConnection.cursor()
		sql = "INSERT INTO `foodinfo_db` (`category`, `description`, `energy`, `fat`, `saturates`, `carbohydrate`, `sugars`, `fibre`, `protein`, `salt` ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		cursor.execute(sql, (inputFood.category,inputFood.description,inputFood.energy,inputFood.fat,inputFood.saturates,inputFood.carbohydrate,inputFood.sugars,inputFood.fibre,inputFood.protein,inputFood.salt) )
		newFoodID = serverConnection.insert_id()
		serverConnection.commit()
		serverConnection.close()
		newFood = food_getInfo(newFoodID)
		return (True,newFood[1])
	except:
		return (False,0)

def food_getInfo(itemID):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT * FROM `foodinfo_db` WHERE `id`=%s"
	cursor.execute(sql,(itemID))
	sqlResult = cursor.fetchone()
	serverConnection.close()
	if (sqlResult is None) : 
		return (False,0)
	else:
		returnFood = foodDataStructure(sqlResult['id'],sqlResult['category'],sqlResult['description'],sqlResult['energy'],sqlResult['fat'],sqlResult['saturates'],sqlResult['carbohydrate'],sqlResult['sugars'],sqlResult['fibre'],sqlResult['protein'],sqlResult['salt'])
		return (True, returnFood)

def food_searchByDescription(description):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT * FROM `foodinfo_db` WHERE `description` LIKE %s"
	cursor.execute(sql,(description))
	sqlResult = cursor.fetchall()
	serverConnection.close()
	return sqlResult

def food_searchByCategory(category):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT * FROM `foodinfo_db` WHERE `category` LIKE %s"
	cursor.execute(sql,(category))
	sqlResult = cursor.fetchall()
	serverConnection.close()
	return sqlResult
		
class foodDataStructure:
	def __init__(self, id=0, category="", description="", energy="0", fat="0", saturates="0", carbohydrate="0", sugars="0", fibre="0", protein="0", salt="0"):
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


#~ food_searchByCategory("frui")
#~ print (food_searchByDescription("apple"))
#~ food = food_getInfo("35")
#~ print (food)
#~ food[1].printFoodDetails()
#~ inputFood = foodDataStructure()
#~ food_register(inputFood)
	
