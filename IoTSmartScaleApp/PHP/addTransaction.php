<?php
$con = mysqli_connect("solarpaygogo.com","spgg_user","spgg_user","solarpaygogo_db");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$serialNum = $_GET['serialNum'];
$activationCode = $_GET['activationCode'];
$numOfHours = $_GET['numOfHours'];
$issueBy = $_GET['issueBy'];
$issueAt = $_GET['issueAt'];
$expireAt = $_GET['expireAt'];

$sql = "SELECT `serialNum` FROM `device` WHERE `serialNum` = " . $serialNum;
$result = mysqli_query($con, $sql);
$row = mysqli_fetch_array($result);

if ($row[0] != null){
	$sql = "INSERT INTO transaction (serialNum, activationCode, numOfHours, issueBy, issueAt, expireAt) 
	VALUES (" . $serialNum . "," . $activationCode . "," . $numOfHours . "," . $issueBy . ",". $issueAt . "," . $expireAt .")";

	if ($con->query($sql) === TRUE) {
	    echo "SUCCESS";
	} else {
	    echo "Error: " . $sql . "<br>" . $con->error;
	}
} else {
	echo "Error: Serial Number not exist on database";
}


mysqli_close($con);
?>