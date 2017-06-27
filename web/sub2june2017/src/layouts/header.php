<div id="header">
  <h1>Welcome to Exam</h1>
  <?php if(array_key_exists("error", $_SESSION)) { ?>
    <p>
      Error: <?php echo $_SESSION['error'] ?>
      <?php unset($_SESSION['error'])?>
    </p>
  <?php } if(array_key_exists("user", $_SESSION)) { ?>
    <p>
      Logged in as <?php echo $_SESSION["user"]?> <br />
      ID = <?php echo $_SESSION["user_id"]?>
    </p>
  <?php } else { ?>
      <a href="./login.php">Login</a>
      <a href="./register.php">Register</a>
  <?php } ?>
  <a href="#">Chat</a>
  <a href="./logout.php">Logout</a>
</div>
