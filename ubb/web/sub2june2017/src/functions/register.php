<?php
  session_start();

  $user = $_POST['user'];
  $question = $_POST['question'];
  $answer = $_POST['answer'];

  if(is_null($user) || empty($user)) {
    $_SESSION["error"] = "Please insert a non-empty username!";
    header("Location: ../index.php");
    return ;
  }

  if(is_null($question) || empty($question)) {
    $_SESSION["error"] = "Please insert a non-empty question!";
    header("Location: ../index.php");
    return ;
  }

  if(is_null($answer) || empty($answer)) {
    $_SESSION["error"] = "Please insert a non-empty answer!";
    header("Location: ../index.php");
    return ;
  }

  include './connect.php';
  $con = connect();
  $stmt = $con->prepare("INSERT INTO Users(user, secretQuestion, secretAnswer) VALUES ('$user', '$question', '$answer')");
  if($stmt->execute()) {
    $_SESSION["user"] = $user;
    $_SESSION["user_id"] = $con->lastInsertId();
    unset($_SESSION["error"]);
    header("Location: ../index.php");
  }
  else {
    $_SESSION["error"] = "There was an error, please insert all the fields!";
    header("Location: ../index.php");
  }
?>
