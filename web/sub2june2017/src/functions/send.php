<?php
  session_start();

  $sender = $_POST['sender'];
  $type = $_POST['type'];
  $text = $_POST['text'];
  $receivers = $_POST['receivers'];

  echo $sender;
  echo $type;
  echo $receivers;

  include './connect.php';

  $con = connect();
  $stmt = $con->prepare("INSERT INTO Messages(sender, type, receivers, text) VALUES ('$sender', '$type', '$receivers', '$text')");
  if(!$stmt->execute()) {
    $_SESSION["error"] = "There was an error sending messages";
    header("Location: ../index.php");
    return ;
  }
  $_SESSION["message_sent"] = "Succesfully sent message";
  header("Location: ../chat.php");
?>
