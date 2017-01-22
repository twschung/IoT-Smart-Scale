import pymysql.cursors, time , db_structure, sqlite3

def connectToServer():
	connection = pymysql.connect(host='151.236.63.243',user='terminal_user',password='abcd1234',db='smartscale',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	return connection

def user_login(inputUsername, inputPassword):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT * FROM `userinfo_db` WHERE `username`=%s AND `password`=%s"
	cursor.execute(sql,(inputUsername,inputPassword))
	sqlResult = cursor.fetchone()
	serverConnection.close()
	if (sqlResult is None) :
		#print ("Fail to fetch user details from DB (Incorrect Username or Password)")
		return (False,0)
	else:
		returnUser = db_structure.userDataStructure(sqlResult['id'],sqlResult['username'],sqlResult['password'],sqlResult['email'],sqlResult['firstname'],sqlResult['lastname'],sqlResult['dob'],sqlResult['gender'],sqlResult['height'],sqlResult['weight'],sqlResult['targetWeight'],sqlResult['targetIntake'])
		return (True, returnUser)

def user_checkIfEmailAlreadyRegisted(inputEmail):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT id FROM `userinfo_db` WHERE `username`=%s"
	cursor.execute(sql,(inputEmail))
	sqlResult = cursor.fetchone()
	serverConnection.close()
	if (sqlResult is None):
		return False
	else:
		return True

def user_register(inputUser):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT id FROM `userinfo_db` WHERE `username`=%s"
	cursor.execute(sql,(inputUser.username))
	sqlResult = cursor.fetchone()
	if (sqlResult is None):
		sql = "INSERT INTO `userinfo_db` (`username`, `password`, `email`, `firstname`, `lastname`, `dob`, `gender`, `height`, `weight`, `targetWeight`, `targetIntake`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		cursor.execute(sql, (inputUser.username,inputUser.password,inputUser.email,inputUser.firstname,inputUser.lastname,inputUser.dob,inputUser.gender,inputUser.height,inputUser.weight,inputUser.targetWeight,inputUser.targetIntake) )
		serverConnection.commit()
		serverConnection.close()
		return (True,0)
	else:
		serverConnection.close()
		return (False,0)

def user_changeUserDetails(inputUser):
	verifedUser = user_login(inputUser.username,inputUser.password)
	if (verifedUser[0] == False):
		return (False,0)
	else:
		serverConnection = connectToServer()
		cursor = serverConnection.cursor()
		sql = "UPDATE `userinfo_db` SET `email`=%s , `firstname`=%s , `lastname`=%s , `dob`=%s , `gender`=%s , `height`=%s , `weight`=%s , `targetWeight`=%s , `targetIntake`=%s WHERE id = %s"
		cursor.execute(sql, (inputUser.email, inputUser.firstname, inputUser.lastname, inputUser.dob, inputUser.gender, inputUser.height, inputUser.weight, inputUser.targetWeight, inputUser.targetIntake, verifedUser[1].id))
		serverConnection.commit()
		serverConnection.close()
		comfirmUser = user_login(verifedUser[1].username, verifedUser[1].password)
		return (True,comfirmUser[1])
		# if (comfirmUser[1] == inputUser) :
			# return (True,comfirmUser[1])
		# else:
			# return (False,1)

def user_changePassword(inputUser):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "UPDATE `userinfo_db` SET `password`=%s WHERE id = %s"
	cursor.execute(sql, (inputUser.password,inputUser.id))
	serverConnection.commit()
	serverConnection.close()
	comfirmUser = user_login(inputUser.username, inputUser.password)
	if (comfirmUser[0] == False):
		return (False,1)
	else:
		return (True, comfirmUser[1])

def food_getInfo_localDB(itemID):
	serverConnection = sqlite3.connect('localFoodDB.db')
	serverConnection.row_factory = sqlite3.Row
	cursor = serverConnection.cursor()
	cursor.execute("SELECT * FROM `foodinfo_db` WHERE `id`=%s"%(itemID))
	sqlResult = cursor.fetchone()
	serverConnection.close()
	if (sqlResult is None) :
		return (False,0)
	else:
		returnFood = db_structure.foodDataStructure(sqlResult['id'],sqlResult['category'],sqlResult['description'],sqlResult['energy'],sqlResult['fat'],sqlResult['saturates'],sqlResult['carbohydrate'],sqlResult['sugars'],sqlResult['fibre'],sqlResult['protein'],sqlResult['salt'])
		return (True, returnFood)

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
		returnFood = db_structure.foodDataStructure(sqlResult['id'],sqlResult['category'],sqlResult['description'],sqlResult['energy'],sqlResult['fat'],sqlResult['saturates'],sqlResult['carbohydrate'],sqlResult['sugars'],sqlResult['fibre'],sqlResult['protein'],sqlResult['salt'])
		return (True, returnFood)

def user_getDailyIntake(userId, date):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT * FROM `userdailyintake_db` WHERE `userid`=%s AND `date`=%s"
	cursor.execute(sql,(userId, date))
	sqlResult = cursor.fetchone()
	serverConnection.close()
	if (sqlResult is None) :
		return (False,0)
	else:
		returnDailyIntake = db_structure.userDailyIntakeStructure(sqlResult['id'],sqlResult['userid'],sqlResult['date'],sqlResult['energy'],sqlResult['fat'],sqlResult['saturates'],sqlResult['carbohydrate'],sqlResult['sugars'],sqlResult['fibre'],sqlResult['protein'],sqlResult['salt'])
		return (True, returnDailyIntake)

def food_getActualInfo(userId,foodId,weight):
	foodInfo = food_getInfo_localDB(foodId)[1]
	actualFoodInfo = db_structure.userFoodIntakeStructure()
	actualFoodInfo.userid = userId
	actualFoodInfo.datetime = time.strftime('%Y-%m-%d %H:%M:%S')
	actualFoodInfo.foodid = foodId
	actualFoodInfo.weight = weight
	weight = float(weight) / 100
	actualFoodInfo.foodcategory = foodInfo.category
	actualFoodInfo.fooddescription = foodInfo.description
	actualFoodInfo.energy = float(weight) * float (foodInfo.energy)
	actualFoodInfo.fat = float(weight) * float (foodInfo.fat)
	actualFoodInfo.saturates = float(weight) * float (foodInfo.saturates)
	actualFoodInfo.carbohydrate = float(weight) * float (foodInfo.carbohydrate)
	actualFoodInfo.sugars = float(weight) * float (foodInfo.sugars)
	actualFoodInfo.fibre = float(weight) * float (foodInfo.fibre)
	actualFoodInfo.protein = float(weight) * float (foodInfo.protein)
	actualFoodInfo.salt = float(weight) * float (foodInfo.salt)
	return actualFoodInfo

def user_addNewFoodIntake(actualFoodInfo):
	currentUserDailyIntake = user_getDailyIntake(actualFoodInfo.userid, time.strftime('%Y-%m-%d'))
	if (currentUserDailyIntake[0]==True):
		newRecord = False
		currentUserDailyIntake = currentUserDailyIntake[1]
	else:
		newRecord = True
		currentUserDailyIntake = db_structure.userDailyIntakeStructure()
		currentUserDailyIntake.userid = actualFoodInfo.userid
		currentUserDailyIntake.date = time.strftime('%Y-%m-%d')
	currentUserDailyIntake.energy = float(currentUserDailyIntake.energy) + float(actualFoodInfo.energy)
	currentUserDailyIntake.fat = float(currentUserDailyIntake.fat) + float(actualFoodInfo.fat)
	currentUserDailyIntake.saturates = float(currentUserDailyIntake.saturates) + float(actualFoodInfo.saturates)
	currentUserDailyIntake.carbohydrate = float(currentUserDailyIntake.carbohydrate) + float(actualFoodInfo.carbohydrate)
	currentUserDailyIntake.sugars = float(currentUserDailyIntake.sugars) + float(actualFoodInfo.sugars)
	currentUserDailyIntake.fibre = float(currentUserDailyIntake.fibre) + float(actualFoodInfo.fibre)
	currentUserDailyIntake.protein = float(currentUserDailyIntake.protein) + float(actualFoodInfo.protein)
	currentUserDailyIntake.salt = float(currentUserDailyIntake.salt) + float(actualFoodInfo.salt)
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "INSERT INTO `userfoodintake_db` (`userid`, `datetime`, `foodid`, `weight`, `foodcategory`, `fooddescription`, `energy`, `fat`, `saturates`, `carbohydrate`, `sugars`, `fibre`, `protein`, `salt`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	cursor.execute(sql, (actualFoodInfo.userid,actualFoodInfo.datetime,actualFoodInfo.foodid,actualFoodInfo.weight,actualFoodInfo.foodcategory,actualFoodInfo.fooddescription,actualFoodInfo.energy,actualFoodInfo.fat,actualFoodInfo.saturates,actualFoodInfo.carbohydrate,actualFoodInfo.sugars,actualFoodInfo.fibre,actualFoodInfo.protein,actualFoodInfo.salt) )
	serverConnection.commit()
	if (newRecord == True):
		sql = "INSERT INTO `userdailyintake_db` (`userid`, `date`, `energy`, `fat`, `saturates`, `carbohydrate`, `sugars`, `fibre`, `protein`, `salt`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		cursor.execute(sql, (currentUserDailyIntake.userid,currentUserDailyIntake.date,currentUserDailyIntake.energy,currentUserDailyIntake.fat,currentUserDailyIntake.saturates,currentUserDailyIntake.carbohydrate,currentUserDailyIntake.sugars,currentUserDailyIntake.fibre,currentUserDailyIntake.protein,currentUserDailyIntake.salt) )
		serverConnection.commit()
	else:
		sql = "UPDATE `userdailyintake_db` SET `energy`=%s, `fat`=%s, `saturates`=%s, `carbohydrate`=%s, `sugars`=%s, `fibre`=%s, `protein`=%s, `salt`=%s WHERE id = %s"
		cursor.execute(sql, (currentUserDailyIntake.energy,currentUserDailyIntake.fat,currentUserDailyIntake.saturates,currentUserDailyIntake.carbohydrate,currentUserDailyIntake.sugars,currentUserDailyIntake.fibre,currentUserDailyIntake.protein,currentUserDailyIntake.salt,currentUserDailyIntake.id))
		serverConnection.commit()
	serverConnection.close()
	return (True,currentUserDailyIntake)

def user_getRangeFoodIntake (userId, startDateTime, endDateTime):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT * FROM `userfoodintake_db` WHERE `userid`=%s AND `datetime` BETWEEN %s AND %s"
	cursor.execute(sql,(userId, startDateTime, endDateTime))
	sqlResult = cursor.fetchall()
	serverConnection.close()
	if (sqlResult is None) :
		return (False,0)
	else:
		if (len(sqlResult) > 0):
			returnfoodIntake = ()
			for i in range(0,(len(sqlResult))):
				returnfoodIntake =returnfoodIntake + (db_structure.userFoodIntakeStructure(sqlResult[i]['id'], \
				sqlResult[i]['userid'],sqlResult[i]['datetime'],sqlResult[i]['foodid'],sqlResult[i]['weight'], \
				sqlResult[i]['foodcategory'],sqlResult[i]['fooddescription'],sqlResult[i]['energy'], \
				sqlResult[i]['fat'],sqlResult[i]['saturates'],sqlResult[i]['carbohydrate'],sqlResult[i]['sugars'], \
				sqlResult[i]['fibre'],sqlResult[i]['protein'],sqlResult[i]['salt']),)
			return(True, returnfoodIntake)
		else:
			return (False, 0)

def user_getRangeDailyIntake (userId, startDate, endDate):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT * FROM `userdailyintake_db` WHERE `userid`=%s AND `date` BETWEEN %s AND %s"
	cursor.execute(sql,(userId, startDate, endDate))
	sqlResult = cursor.fetchall()
	serverConnection.close()
	if (sqlResult is None) :
		return (False,0)
	else:
		if (len(sqlResult) > 0):
			returnRangeDailyIntake = ()
			for i in range(0,(len(sqlResult))):
				returnRangeDailyIntake =returnRangeDailyIntake + (db_structure.userDailyIntakeStructure( \
				sqlResult[i]['id'],sqlResult[i]['userid'],sqlResult[i]['date'],sqlResult[i]['energy'], \
				sqlResult[i]['fat'],sqlResult[i]['saturates'],sqlResult[i]['carbohydrate'],sqlResult[i]['sugars'], \
				sqlResult[i]['fibre'],sqlResult[i]['protein'],sqlResult[i]['salt']),)
			return(True, returnRangeDailyIntake)
		else:
			return (False, 0)

def user_removeFoodIntake(removeFoodInTake):
	currentUserDailyIntake = user_getDailyIntake(removeFoodInTake.userid,removeFoodInTake.datetime.strftime('%Y-%m-%d'))
	if (currentUserDailyIntake[0]==True):
		currentUserDailyIntake = currentUserDailyIntake[1]
		currentUserDailyIntake.energy = float(currentUserDailyIntake.energy) - float(removeFoodInTake.energy)
		currentUserDailyIntake.fat = float(currentUserDailyIntake.fat) - float(removeFoodInTake.fat)
		currentUserDailyIntake.saturates = float(currentUserDailyIntake.saturates) - float(removeFoodInTake.saturates)
		currentUserDailyIntake.carbohydrate = float(currentUserDailyIntake.carbohydrate) - float(removeFoodInTake.carbohydrate)
		currentUserDailyIntake.sugars = float(currentUserDailyIntake.sugars) - float(removeFoodInTake.sugars)
		currentUserDailyIntake.fibre = float(currentUserDailyIntake.fibre) - float(removeFoodInTake.fibre)
		currentUserDailyIntake.protein = float(currentUserDailyIntake.protein) - float(removeFoodInTake.protein)
		currentUserDailyIntake.salt = float(currentUserDailyIntake.salt) - float(removeFoodInTake.salt)
		serverConnection = connectToServer()
		cursor = serverConnection.cursor()
		sql = "UPDATE `userdailyintake_db` SET `energy`=%s, `fat`=%s, `saturates`=%s, `carbohydrate`=%s, `sugars`=%s, `fibre`=%s, `protein`=%s, `salt`=%s WHERE id = %s"
		cursor.execute(sql, (currentUserDailyIntake.energy,currentUserDailyIntake.fat,currentUserDailyIntake.saturates,currentUserDailyIntake.carbohydrate,currentUserDailyIntake.sugars,currentUserDailyIntake.fibre,currentUserDailyIntake.protein,currentUserDailyIntake.salt,currentUserDailyIntake.id))
		serverConnection.commit()
		sql = "DELETE FROM `userfoodintake_db` WHERE `id`=%s"
		cursor.execute(sql, (removeFoodInTake.id))
		serverConnection.commit()
		serverConnection.close()
		return (True, 0)
	else:
		return (False, 0)



# result = user_getRangeFoodIntake("1", "2016-11-04", "2016-11-05")
# result = result[1][0]
# result = user_removeFoodIntake(result)
# print (result[0])
# foodInfo = food_getActualInfo("1","1","200")
# user_addNewFoodIntake(foodInfo)
# testuser = db_structure.userDataStructure("2","qq","ee","321","321","321","321","321","321","321")
# user_changeUserDetails (testuser)
# user_changePassword(testuser,"ww","ee")
# user_register(testuser)
