<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
</head>
<body>
  <form action="./functions/register.php" method="post">
    <label>Username</label>
    <input type="text" name="user" />
    <br />
    <label>Secret Question</label>
    <input type="text" name="question" />
    <br />
    <label>Secret Answer</label>
    <input type="text" name="answer" />
    <br />
    <input type="submit" value="Register" />
  </form>
</body>
</html>
