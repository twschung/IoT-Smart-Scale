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
		return False
	else:
		returnUser = db_structure.userDataStructure(sqlResult['id'],sqlResult['username'],sqlResult['password'],sqlResult['email'],sqlResult['firstname'],sqlResult['lastname'],sqlResult['dob'],sqlResult['gender'],sqlResult['height'],sqlResult['weight'])
		return returnUser
