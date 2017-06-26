<?php
  session_start();
  $user = $_POST['user'];
  $pass = $_POST['password'];
  echo $user;
  echo $pass;
  /// todo: connect to db
  $_SESSION["user"] = $user;
  header("Location: ../index.php");
?>
