<?php
  include 'connect.php';

  $user = $_GET['user'];

  $con = connect();
  $stmt = $con->prepare("SELECT * FROM Messages WHERE sender = '$user'
            AND type = 'unicast'
            AND receivers = views");
  $stmt->execute();
  die(json_encode($stmt->fetchAll()));
?>
