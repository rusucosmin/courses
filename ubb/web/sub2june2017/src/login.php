<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
</head>
<body>
  <form action="./functions/login.php" method="post">
    <label>Username</label>
    <input type="text" name="user" />
    <br />
    <input type="submit" value="Login" />
  </form>
</body>
</html>
