<?php
$con = mysqli_connect("151.236.63.243","terminal_user","abcd1234","smartscale");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$id = $_GET['id'];
$firstname = $_GET['firstname'];
$lastname = $_GET['lastname'];
$dob = $_GET['dob'];
$gender = $_GET['gender'];
$height = $_GET['height'];
$weight = $_GET['weight'];
$targetweight = $_GET['targetweight'];
$targetintake = $_GET['targetintake'];

$sql = "UPDATE user SET firstname =" . $firstname . " and lastname =" . $lastname ." and dob =" . $dob ." and gender =" . $gender ." and height =" . $height ." and weight =" . $weight ." and targetweight =" . $targetweight ." and targetintake =" . $targetintake ." WHERE id =" . $id;

if ($con->query($sql) === TRUE) {
    echo "SUCCESS";
} else {
    echo "Error: " . $sql . "<br>" . $con->error;
}

mysqli_close($con);
?>