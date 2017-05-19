<?php
	session_start();

	require_once '../functions/read.php';

	$query = $_GET['query'];
	if ($query == null) {
		$query = "";
	}
	$cars = get_all_cars($query);

	exit(json_encode($cars));
?>
