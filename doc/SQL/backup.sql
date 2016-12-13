CREATE TABLE smartscale.foodinfo_db (
	id int(10) NOT NULL auto_increment,
	category varchar(25),
	description varchar(50),
	energy varchar(25),
	fat varchar(25),
	saturates varchar(25),
	carbohydrate varchar(25),
	sugars varchar(25),
	fibre varchar(25),
	protein varchar(25),
	salt varchar(25)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 RAZORSEP~!@#*^$
CREATE TABLE smartscale.userdailyintake_db (
	id int(10) NOT NULL auto_increment,
	userid varchar(25),
	date date,
	energy varchar(25),
	fat varchar(25),
	saturates varchar(25),
	carbohydrate varchar(25),
	sugars varchar(25),
	fibre varchar(25),
	protein varchar(25),
	salt varchar(25)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 RAZORSEP~!@#*^$
CREATE TABLE smartscale.userfoodintake_db (
	id int(10) NOT NULL auto_increment,
	userid varchar(25),
	datetime datetime,
	foodid varchar(25),
	weight varchar(25),
	foodcategory varchar(25),
	fooddescription varchar(25),
	energy varchar(25),
	fat varchar(25),
	saturates varchar(25),
	carbohydrate varchar(25),
	sugars varchar(25),
	fibre varchar(25),
	salt varchar(25),
	protein varchar(25)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 RAZORSEP~!@#*^$
CREATE TABLE smartscale.userinfo_db (
	id int(10) NOT NULL auto_increment,
	username varchar(25),
	password varchar(25),
	email varchar(50),
	firstname varchar(50),
	lastname varchar(50),
	dob varchar(25),
	gender varchar(5),
	height varchar(5),
	weight varchar(5),
	targetWeight varchar(25),
	targetIntake varchar(25)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (1, '', 'apple', '52', '0', '0', '14', '10', '2', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (2, '', 'orange', '47', '0', '0', '12', '9', '2', '1', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (3, '', 'banana', '89', '0', '0', '23', '12', '3', '1', '0.001') RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (4, '', 'pear', '42', '0', '0', '11', '7', '4', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (5, '', 'mango', '65', '0', '0', '17', '15', '2', '1', '0.002') RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (6, '', 'pumpkin', '23', '0.1', '0.1', '7', '2.8', '0.5', '1', '0.001') RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (7, '', 'tomato', '18', '0.2', '0', '3.9', '2.6', '0.9', '0.9', '0.005') RAZORSEP~!@#*^$
INSERT INTO smartscale.foodinfo_db(id, category, description, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (8, '', 'broccoli', '34', '0.4', '0', '7', '1.7', '2.6', '2.8', '0.033') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (2, '1', '2016-12-08', '52', '0', '0', '14', '10', '2', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (6, '1', '2016-12-07', '123', '1', '1', '1', '2', '3', '2', '1') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (7, '1', '2016-12-06', '23', '1', '3', '2', '4', '5', '3', '2') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (8, '1', '2016-12-05', '1345', '1', '12', '2', '3', '2', '3', '34') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (9, '1', '2016-12-04', '234', '2', '2', '22', '2', '2', '2', '2') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (10, '1', '2016-12-03', '898', '79', '78', '9', '89', '89', '78', '78') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (11, '1', '2016-12-02', '345', '34', '34', '56', '76', '56', '56', '67') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (12, '1', '2016-12-01', '753', '32', '43', '1', '24', '32', '43', '2') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (13, '1', '2016-11-30', '387', '89', '890', '90', '89', '89', '09', '89') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (14, '1', '2016-11-29', '23', '89', '34', '53', '876', '98', '8', '87') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (15, '1', '2016-11-28', '235', '75', '95', '7', '98', '55', '82', '73') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (16, '1', '2016-11-27', '65', '94', '08', '9', '9', '9', '8', '7') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (17, '1', '2016-11-26', '2000', '87', '89', '87', '88', '9', '8', '8') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (18, '1', '2016-11-25', '874', '72', '67', '87', '87', '78', '67', '76') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (19, '5', '2016-12-09', '45.59', '0', '0', '11.64', '8.73', '1.94', '0.97', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (20, '1', '2016-12-11', '453', '2', '2', '1', '3', '3', '2', '2') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (21, '1', '2016-12-09', '1876', '12', '98', '87', '9', '8', '23', '3') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (22, '1', '2016-12-10', '323', '32', '34', '23', '34', '23', '43', '3') RAZORSEP~!@#*^$
INSERT INTO smartscale.userdailyintake_db(id, userid, date, energy, fat, saturates, carbohydrate, sugars, fibre, protein, salt) VALUES (23, '1', '2016-12-12', '234', '89', '32', '043', '43', '43', '43', '34') RAZORSEP~!@#*^$
INSERT INTO smartscale.userfoodintake_db(id, userid, datetime, foodid, weight, foodcategory, fooddescription, energy, fat, saturates, carbohydrate, sugars, fibre, salt, protein) VALUES (1, '5', '2016-12-07 21:20:06', '1', '100', '', 'apple', '52', '0', '0', '14', '10', '2', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userfoodintake_db(id, userid, datetime, foodid, weight, foodcategory, fooddescription, energy, fat, saturates, carbohydrate, sugars, fibre, salt, protein) VALUES (2, '1', '2016-12-08 00:45:59', '1', '100', '', 'apple', '52', '0', '0', '14', '10', '2', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userfoodintake_db(id, userid, datetime, foodid, weight, foodcategory, fooddescription, energy, fat, saturates, carbohydrate, sugars, fibre, salt, protein) VALUES (3, '5', '2016-12-08 11:42:28', '1', '55', '', 'apple', '28.6', '0', '0', '7.7', '5.5', '1.1', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userfoodintake_db(id, userid, datetime, foodid, weight, foodcategory, fooddescription, energy, fat, saturates, carbohydrate, sugars, fibre, salt, protein) VALUES (4, '5', '2016-12-09 14:23:42', '2', '97', '', 'orange', '45.59', '0', '0', '11.64', '8.73', '1.94', '0', '0.97') RAZORSEP~!@#*^$
INSERT INTO smartscale.userinfo_db(id, username, password, email, firstname, lastname, dob, gender, height, weight, targetWeight, targetIntake) VALUES (1, 'twschung@gmail.com', '0000', 'twschung@gmail.com', 'Terry', 'Chung', '1994', 'm', '1.63', '70', '65', '2000') RAZORSEP~!@#*^$
INSERT INTO smartscale.userinfo_db(id, username, password, email, firstname, lastname, dob, gender, height, weight, targetWeight, targetIntake) VALUES (2, '.@', '1234', '.@', 'm', 'm', '1665', 'm', '128', '125', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userinfo_db(id, username, password, email, firstname, lastname, dob, gender, height, weight, targetWeight, targetIntake) VALUES (3, 'sv@.c', '0000', 'sv@.c', 'sel', 'tan', '1994', 'm', '160', '50', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userinfo_db(id, username, password, email, firstname, lastname, dob, gender, height, weight, targetWeight, targetIntake) VALUES (4, 's@com', '0000', 's@com', 'selena', 'tan', '1994', 'f', '1.58', '50', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userinfo_db(id, username, password, email, firstname, lastname, dob, gender, height, weight, targetWeight, targetIntake) VALUES (5, 's@tan.com', '0000', 's@tan.com', 'Selena', 'Tan', '1994', 'f', '1.58', '50', '50', '1200') RAZORSEP~!@#*^$
INSERT INTO smartscale.userinfo_db(id, username, password, email, firstname, lastname, dob, gender, height, weight, targetWeight, targetIntake) VALUES (6, 'x@hoong.com', '0000', 'x@hoong.com', 'Xuen', 'K', '1994', 'm', '1.7', '150', '0', '0') RAZORSEP~!@#*^$
INSERT INTO smartscale.userinfo_db(id, username, password, email, firstname, lastname, dob, gender, height, weight, targetWeight, targetIntake) VALUES (7, 's@f.com', '1234', 's@f.com', 'se', 'tan', '1994', 'm', '1.8', '75', '', '') RAZORSEP~!@#*^$
