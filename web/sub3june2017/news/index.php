<?php
  session_start();
  if(array_key_exists('user', $_SESSION)) {
    // check type of user then
    if($_SESSION['user_id'] == 1) {
      header("Location: add.php");
    } else if($_SESSION['user_id'] == 2) {
      header("Location: view.php");
    }
  }
?>
<!DOCTYPE html>
<head>
  <?php
  ?>
</head>
<body>
  <div id="header">
    Welcome to news, please login
  </div>
  <?php
    if(array_key_exists('user', $_SESSION)) { ?>
      <p>
        Logged in as <?php echo $_SESSION['user']?>
      </p>
  <?php } else { ?>
      <form action="./forms/login.php" method="post">
        <label>user</label>
        <input name="user" type="text" />
        <br />
        <label>password</label>
        <input name="password" type="password" />
        <br />
        <input type="submit" value="Login" />
      </form>
  <?php } ?>
</body>
