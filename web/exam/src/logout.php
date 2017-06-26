<?php
  session_start();
  // TODO: clear all the cookies (user, errors, etc)
  unset($_SESSION["user"]);
  unset($_SESSION["user_id"]);
  unset($_SESSION["error"]);
  header("Location: ./index.php");
?>
