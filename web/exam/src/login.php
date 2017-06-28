<?php
  session_start();
?>

<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
</head>
<body>
  <?php include './layouts/header.php'; ?>
  <h1>Log in</h1>
  <div id="content">
    <form action="./functions/login.php" method="post">
      <label>Username</label>
      <input type="text" name="user" />
      <br />
      <label>Password</label>
      <input type="password" name="password" />
      <br />
      <input type="submit" value="Login" />
    </form>
  </div>
  <?php include './layouts/footer.php'; ?>
</body>
</html>
