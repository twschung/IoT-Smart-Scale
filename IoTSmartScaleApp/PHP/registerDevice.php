<?php
$con = mysqli_connect("solarpaygogo.com","spgg_user","spgg_user","solarpaygogo_db");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$serialNum = $_GET['serialNum'];
$devicePhoneNum = $_GET['devicePhoneNum'];
$privateKey = $_GET['privateKey'];
$timezone = $_GET['timezone'];
$clientFirsName = $_GET['clientFirsName'];
$clientLastName = $_GET['clientLastName'];
$clientPhoneNum = $_GET['clientPhoneNum'];
$clientEmail = $_GET['clientEmail'];
$APNname = $_GET['APNname'];
$APNusername = $_GET['APNusername'];
$APNpassword = $_GET['APNpassword'];
$FTPaddress = $_GET['FTPaddress'];
$FTPport = $_GET['FTPport'];
$FTPusername = $_GET['FTPusername'];
$FTPpassword = $_GET['FTPpassword'];
$FTPpath = $_GET['FTPpath'];
$TimeUploadHH = $_GET['TimeUploadHH'];
$TimeUploadMM = $_GET['TimeUploadMM'];
$createdBy = $_GET['createdBy'];
$createdAt = $_GET['createdAt'];
$updateBy = $_GET['updateBy'];
$updateAt = $_GET['updateAt'];

$sql = "SELECT `serialNum` FROM `device` WHERE `serialNum` = " . $serialNum;
$result = mysqli_query($con, $sql);
$row = mysqli_fetch_array($result);

if ($row[0] == null){
	$sql = "INSERT INTO device (serialNum, devicePhoneNum, privateKey, timezone, clientFirstName, clientLastName, clientPhoneNum, clientEmail, APNname, APNusername, APNpassword, FTPaddress, FTPport, FTPusername, FTPpassword, FTPpath, TimeUploadHH, TimeUploadMM, createdBy, createdAt, updateBy,updateAt) 
	VALUES (" . $serialNum . "," . $devicePhoneNum . "," . $privateKey . "," . $timezone . ",". $clientFirsName . "," . $clientLastName . "," . $clientPhoneNum . "," . $clientEmail . "," . $APNname . "," . $APNusername . "," . $APNpassword . "," . $FTPaddress . "," . $FTPport . "," . $FTPusername . "," . $FTPpassword . "," . $FTPpath . "," . $TimeUploadHH . "," . $TimeUploadMM . "," . $createdBy . "," . $createdAt . "," . $updateBy . "," . $updateAt .")";

	if ($con->query($sql) === TRUE) {
	    echo "SUCCESS";
	} else {
	    echo "Error: " . $sql . "<br>" . $con->error;
	}
} else {
	echo "Error: same serialNum exist on database";
}


mysqli_close($con);
?>