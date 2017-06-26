<?php
  session_start();

  $user = $_POST['user'];
  $password = $_POST['password'];

  echo $user;
  echo $password;

  include './connect.php';
  $con = connect();
  $stmt = $con->prepare("SELECT * FROM test_users WHERE user='$user' AND password='$password'");
  $stmt->execute();
  if($stmt->rowCount() > 0) {
    $uObj = $stmt->fetch(PDO::FETCH_OBJ);
    $_SESSION["user"] = $uObj->user;
    $_SESSION["user_id"] = $uObj->ID;
  }
  else {
    $_SESSION["error"] = "User and/or password are incorrect";
  }
  header("Location: ../index.php");
?>
