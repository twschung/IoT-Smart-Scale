import pymysql.cursors , db_structure

def connectToServer():
	connection = pymysql.connect(host='localhost',user='admin',password='abcd1234',db='smartscale',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
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
		returnUser = db_structure.userDataStructure(sqlResult['id'],sqlResult['username'],sqlResult['password'],sqlResult['email'],sqlResult['firstname'],sqlResult['lastname'],sqlResult['dob'],sqlResult['gender'],sqlResult['height'],sqlResult['weight'])
		return (True, returnUser)

def user_register(inputUser):
	serverConnection = connectToServer()
	cursor = serverConnection.cursor()
	sql = "SELECT id FROM `userinfo_db` WHERE `username`=%s"
	cursor.execute(sql,(inputUser.username))
	sqlResult = cursor.fetchone()
	if (sqlResult is None):
		sql = "INSERT INTO `userinfo_db` (`username`, `password`, `email`, `firstname`, `lastname`, `dob`, `gender`, `height`, `weight`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		cursor.execute(sql, (inputUser.username,inputUser.password,inputUser.email,inputUser.firstname,inputUser.lastname,inputUser.dob,inputUser.gender,inputUser.height,inputUser.weight) )
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
		sql = "UPDATE `userinfo_db` SET `email`=%s , `firstname`=%s , `lastname`=%s , `dob`=%s , `gender`=%s , `height`=%s , `weight`=%s WHERE id = %s"
		cursor.execute(sql, (inputUser.email, inputUser.firstname, inputUser.lastname, inputUser.dob, inputUser.gender, inputUser.height, inputUser.weight, verifedUser[1].id))
		serverConnection.commit()
		serverConnection.close()
		comfirmUser = user_login(verifedUser[1].username, verifedUser[1].password)
		return (True,comfirmUser[1])
		# if (comfirmUser[1] == inputUser) :
			# return (True,comfirmUser[1])
		# else:
			# return (False,1)
		
def user_changePassword(inputUser,oldPassword, newPassword):
	verifedUser = user_login(inputUser.username,oldPassword)
	if (verifedUser[0] == False):
		return (False,0)
	else:
		serverConnection = connectToServer()
		cursor = serverConnection.cursor()
		sql = "UPDATE `userinfo_db` SET `password`=%s WHERE id = %s"
		cursor.execute(sql, (newPassword,verifedUser[1].id))
		serverConnection.commit()
		serverConnection.close()
		comfirmUser = user_login(inputUser.username, newPassword)
		if (comfirmUser[0] == False):
			return (False,1)
		else:
			return (True, comfirmUser[1])

	
# testuser = db_structure.userDataStructure("2","qq","ee","321","321","321","321","321","321","321")
# user_changeUserDetails (testuser)
# user_changePassword(testuser,"ww","ee")
# user_register(testuser)