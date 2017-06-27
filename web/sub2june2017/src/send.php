<?php
  session_start();
  if(!array_key_exists("user", $_SESSION)) {
    $_SESSION["error"] = "Please log in first!";
    header("Location: ./index.php");
    return ;
  }
?>
<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
</head>
<body>
  <h1>Send a message</h1>
  <form action="./functions/send.php" method="post">
    <input hidden type="text" name="sender" value="<?php echo $_SESSION["user"]; ?>" />
    <label>Type</label>
    <select name="type">
      <option value="unicast">
        Unicast
      </option>
      <option value="multicast">
        Multicast
      </option>
    </select>
    <br />
    <label>Text</label>
    <input type="text" name="text" />
    <br />
    <label>Receivers(cs-usernames)</label>
    <input type="text" name="receivers" />
    <br />
    <input type="submit" value="Send" />
  </form>
</body>
</html>
