<?php
$con = mysqli_connect("151.236.63.243","terminal_user","abcd1234","smartscale");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$id = $_GET['userid'];
$date = $_GET['date'];

$sql = "SELECT SUM(energy), SUM(fat), SUM(saturates), SUM(carbohydrate), SUM(sugars), SUM(fibre), SUM(protein), SUM(salt) FROM userdailyintake_db WHERE userid = ". $id ." AND date= ". $date ."";

$result = mysqli_query($con, $sql);

while($row = mysqli_fetch_array($result)){
	if($row){
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
	}
	else{
		echo "FAIL";
	}
}

mysqli_close($con);

?>