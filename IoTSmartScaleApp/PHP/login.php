<?php
$con = mysqli_connect("151.236.63.243","terminal_user","abcd1234","smartscale");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$username = $_GET['username'];
$password = $_GET['password'];

$sql = "SELECT * FROM userinfo_db where username = ". $username . " and password = ". $password;
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
	echo "<br>";
	echo $row[7];
	echo "<br>";
	echo $row[8];
	echo "<br>";
	echo $row[9];
	echo "<br>";
	echo $row[10];
	echo "<br>";
	echo $row[11];
	echo "<br>";
	echo $row[12];

} else {
	echo "FAIL";
}

mysqli_close($con);

?>