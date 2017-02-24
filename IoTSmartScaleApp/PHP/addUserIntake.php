<?php
$con = mysqli_connect("151.236.63.243","terminal_user","abcd1234","smartscale");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$id = $_GET['id'];
$fooddescription = $_GET['fooddescription'];
$energy = $_GET['energy'];
$datetime = $_GET['datetime'];

$sql = 
"UPDATE userfoodintake_db SET fooddescription=" . $fooddescription . ",energy=" . $energy .",datetime=" . $datetime .",foodid='0',carbohydrate='0',sugars='0',fibre='0' WHERE userid =" . $id . "";

if ($con->query($sql) === TRUE) {
    echo "SUCCESS";
} else {
    echo "Error: " . $sql . "<br>" . $con->error;
}

mysqli_close($con);
?>