<?php
  session_start();

  $user = $_POST['user'];
  $answer = $_POST['answer'];
  $question = $_POST['question'];


  include './connect.php';

  $con = connect();
  $stmt = $con->prepare("SELECT * FROM Users WHERE user='$user' AND secretQuestion='$question' AND secretAnswer='$answer'");
  $stmt->execute();
  if($stmt->rowCount() > 0) {
    $uObj = $stmt->fetch(PDO::FETCH_OBJ);
    $_SESSION["user"] = $uObj->user;
    $_SESSION["user_id"] = $uObj->id;
    unset($_SESSION["error"]);
  }
  else {
    $_SESSION["error"] = "Secret answer is not valid";
  }
  header("Location: ../index.php");
?>
