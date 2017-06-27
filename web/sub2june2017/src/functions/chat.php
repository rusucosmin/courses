<?php
  include 'connect.php';

  $user = $_GET['user'];

  $con = connect();
  $stmt = $con->prepare("SELECT * FROM Messages WHERE sender = '$user'
            OR (',' + RTRIM(receivers) + ',') LIKE '%,$user,%'");
  $stmt->execute();
  die(json_encode($stmt->fetchAll()));
?>
