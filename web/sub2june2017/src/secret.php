<?php
  session_start();
  if (!array_key_exists("attempt_user", $_SESSION) || !array_key_exists("question", $_SESSION)) {
    unset($_SESSION["attempt_user"]);
    unset($_SESSION["question"]);
    header("Location: login.php");
  }
?>
<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
</head>
<body>
  <form action="./functions/secret.php" method="post">
    <label>Question</label>
    <input tpe="text" name="question" value="<?php echo $_SESSION["question"]; ?>" readonly />
    <br />
    <label>Answer</label>
    <input type="text" name="answer" />
    <br />
    <input type="text" name="user" hidden value="<?php echo $_SESSION["attempt_user"]; ?>" />
    <br />
    <input type="submit" value="Login" />
  </form>
  <?php
    unset($_SESSION["attempt_user"]);
    unset($_SESSION["question"]);
  ?>
</body>
</html>
