<?php
$con = mysqli_connect("solarpaygogo.com","spgg_user","spgg_user","solarpaygogo_db");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$searchIndex = $_GET['searchIndex'];
$searchParam = $_GET['searchParam'];



if ($searchIndex == "'ALL'"){
	$sql = "SELECT `serialNum`, `devicePhoneNum`, `clientFirstName`, `clientLastName`, `clientPhoneNum` FROM `device`";
} else {
	$sql = "SELECT `serialNum`, `devicePhoneNum`, `clientFirstName`, `clientLastName`, `clientPhoneNum` FROM `device` WHERE `" . $searchIndex . "` = " . $searchParam;
}

$result = mysqli_query($con, $sql);

if ($result == TRUE){
	if (mysqli_num_rows($result) > 0) {
		echo "SUCCESS". "<br>";
		while($row = mysqli_fetch_assoc($result)){
			echo $row["serialNum"] . "&nbsp" . $row["devicePhoneNum"] . "&nbsp" . $row["clientFirstName"] . "&nbsp" . $row["clientLastName"] . "&nbsp" . $row["clientPhoneNum"] .  "<br>";
		}
	} else {
		echo "NO RESULT";
	}
} else {
	echo "FAIL";
}

mysqli_close($con);
?>