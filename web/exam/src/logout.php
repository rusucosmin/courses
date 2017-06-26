<?php
  session_start();
  // TODO: clear all the cookies (user, errors, etc)
  unset($_SESSION["user"]);
  header("Location: ./index.php");
?>
