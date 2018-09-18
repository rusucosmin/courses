<?php
  session_start();
  include 'connect.php';

  $con = connect();
  $stmt = $con->prepare("SELECT * FROM Cursuri");
  if(!$stmt->execute()) {
    die(json_encode(array()));
    return ;
  }
  die(json_encode($stmt->fetchAll()));
?>
