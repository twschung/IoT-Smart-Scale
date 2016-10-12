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
		print ("Fail to fetch user details from DB (Incorrect Username or Password)")
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
	
	
# testuser = db_structure.userDataStructure("0","123","123","123","123","123","123","123","123","123")
# user_register(testuser)