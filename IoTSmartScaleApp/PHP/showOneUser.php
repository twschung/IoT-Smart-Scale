<?php
$con = mysqli_connect("solarpaygogo.com","spgg_user","spgg_user","solarpaygogo_db");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$username = $_GET['username'];

$sql = "SELECT id, username, password , firstName, lastName, email, root FROM user where username = ". $username;
$result = mysqli_query($con, $sql);

$row = mysqli_fetch_array($result);
$data = $row[0];

if($data){
	echo "SUCCESS";
	echo "<br>";
	echo $row[0];
	echo "<br>";
	echo $row[1];
	echo "<br>";
	echo $row[2];
	echo "<br>";
	echo $row[3];
	echo "<br>";
	echo $row[4];
	echo "<br>";
	echo $row[5];
	echo "<br>";
	echo $row[6];

} else {
	echo "FAIL";
}

mysqli_close($con);

?>