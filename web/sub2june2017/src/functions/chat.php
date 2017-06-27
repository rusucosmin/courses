<?php
  include 'connect.php';

  $user = $_GET['user'];

  $con = connect();
  $stmt = $con->prepare("SELECT * FROM Messages WHERE sender = '$user'
            OR CONCAT(CONCAT(',', RTRIM(receivers)), ',') LIKE '%,$user,%'");
  $stmt->execute();
  $arr = $stmt->fetchAll();

  $stmt = $con->prepare("UPDATE Messages
                         SET views = '$user'
                         WHERE receivers='$user'
                         AND type='unicast'");
  $stmt->execute();
  die(json_encode($arr));
?>
