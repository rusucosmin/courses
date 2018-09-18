<?php
  include 'connect.php';

  $con = connect();
  $id = $_GET['id'];
  echo $id;
  $stmt = $con->prepare("DELETE FROM news WHERE ID = :id");
  $stmt->execute(array(":id" => $_GET["id"]));
  exit(1);
?>
