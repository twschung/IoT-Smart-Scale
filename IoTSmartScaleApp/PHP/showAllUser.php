<?php
$con = mysqli_connect("solarpaygogo.com","spgg_user","spgg_user","solarpaygogo_db");

if (mysqli_connect_errno($con))
{
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$sql = "SELECT * FROM `user`";
$result = mysqli_query($con, $sql);

if (mysqli_num_rows($result) > 0) {
	echo "SUCCESS". "<br>";
	while($row = mysqli_fetch_assoc($result)){
		echo $row["id"] . "&nbsp" . $row["username"] . "&nbsp" . $row["password"] . "&nbsp" . $row["firstName"] . "&nbsp" . $row["lastName"] . "&nbsp" . $row["email"] . "&nbsp" . $row["root"] .  "<br>";
	}
} else {
	echo "FAIL";
}

mysqli_close($con);
?>
