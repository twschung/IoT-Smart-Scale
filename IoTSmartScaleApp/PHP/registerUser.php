<?php
$con = mysqli_connect("solarpaygogo.com","spgg_user","spgg_user","solarpaygogo_db");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$username = $_GET['username'];
$password = $_GET['password'];
$email = $_GET['email'];
$firstName = $_GET['firstName'];
$lastName = $_GET['lastName'];
$root = $_GET['root'];

$sql = "SELECT `username` FROM `user` WHERE `username` = " . $username;
$result = mysqli_query($con, $sql);
$row = mysqli_fetch_array($result);

if ($row[0] == null){
	$sql = "INSERT INTO user (username, password, firstName, lastName, email, root) 
	VALUES (" . $username . "," . $password . "," . $firstName . "," . $lastName . ",". $email . "," . $root .")";

	if ($con->query($sql) === TRUE) {
	    echo "SUCCESS";
	} else {
	    echo "Error: " . $sql . "<br>" . $con->error;
	}
} else {
	echo "Error: same username exist on database";
}




mysqli_close($con);
?>