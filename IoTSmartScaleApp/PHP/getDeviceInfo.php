<?php
$con = mysqli_connect("solarpaygogo.com","spgg_user","spgg_user","solarpaygogo_db");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$serialNum = $_GET['serialNum'];

$sql = "SELECT * FROM `device` WHERE `serialNum` = " . $serialNum ;

$result = mysqli_query($con, $sql);

if ($result == TRUE){
	if (mysqli_num_rows($result) > 0) {
		echo "SUCCESS". "<br>";
		while($row = mysqli_fetch_assoc($result)){
			echo $row["id"] . "&nbsp" . $row["serialNum"] . "&nbsp" . $row["devicePhoneNum"] . "&nbsp" . $row["privateKey"] . 
			"&nbsp" . $row["timezone"] . "&nbsp" . $row["clientFirstName"] . "&nbsp" . $row["clientLastName"] . "&nbsp" . 
			$row["clientPhoneNum"] . "&nbsp" . $row["clientEmail"] . "&nbsp" . $row["APNname"] . "&nbsp" . $row["APNusername"] . 
			"&nbsp" . $row["APNpassword"] . "&nbsp" . $row["FTPaddress"] . "&nbsp" . $row["FTPport"] . "&nbsp" . $row["FTPusername"] . 
			"&nbsp" . $row["FTPpassword"] . "&nbsp" . $row["FTPpath"] . "&nbsp" . $row["TimeUploadHH"] . "&nbsp" . $row["TimeUploadMM"] . 
			"&nbsp" . $row["createdBy"] . "&nbsp" . $row["createdAt"] . "&nbsp" . $row["updateBy"] . "&nbsp" . $row["updateAt"] . "<br>";
		}
	} else {
		echo "NO RESULT";
	}
} else {
	echo "FAIL";
}

mysqli_close($con);
?>