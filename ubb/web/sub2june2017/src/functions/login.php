<?php
  session_start();

  $user = $_POST['user'];

  include './connect.php';
  $con = connect();
  $stmt = $con->prepare("SELECT * FROM Users WHERE user='$user'");
  $stmt->execute();
  if($stmt->rowCount() > 0) {
    $uObj = $stmt->fetch(PDO::FETCH_OBJ);
    $_SESSION["attempt_user"] = $uObj->user;
    $_SESSION["question"] = $uObj->secretQuestion;
    unset($_SESSION["error"]);
    header("Location: ../secret.php");
  }
  else {
    $_SESSION["error"] = "User and/or password are incorrect";
    header("Location: ../index.php");
  }
?>
