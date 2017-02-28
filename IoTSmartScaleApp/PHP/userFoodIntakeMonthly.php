<?php
$con = mysqli_connect("151.236.63.243","terminal_user","abcd1234","smartscale");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
$id = $_GET['userid'];

/*$sql = "SELECT energy FROM userdailyintake_db WHERE userid =". $id ." AND date >= DATE_SUB(NOW(), INTERVAL 6 MONTH)";*/
$sql = "SELECT SUM(energy), MONTH(`date`), YEAR(`date`) FROM userdailyintake_db WHERE userid =". $id ." AND date >= DATE_SUB(NOW(), INTERVAL 6 MONTH) GROUP BY MONTH(`date`), YEAR(`date`)";

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
	}
	else{
		echo "FAIL";
	}
}

mysqli_close($con);

?>