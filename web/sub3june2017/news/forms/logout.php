<?php
  session_start();
?>
<!DOCTYPE html>
<html>
  <body>
    <?php  unset($_SESSION['user']); ?>
    <p>
      Logged out!
    </p>
  </body>
</htmL>
