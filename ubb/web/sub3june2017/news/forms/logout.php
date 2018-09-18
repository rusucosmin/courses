<?php
  session_start();
?>
<!DOCTYPE html>
<html>
  <body>
    <?php
      unset($_SESSION['user']);
      unset($_SESSION['user_id']);
      unset($_SESSION['user_role']);
      unset($_SESSION['user_password']);
    ?>
    <p>
      Logged out!
    </p>
  </body>
</htmL>
