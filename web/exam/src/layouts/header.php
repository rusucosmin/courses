<div id="header">
  <h1>Welcome to Exam</h1>
  <?php if(array_key_exists("user", $_SESSION)) { ?>
    <p>
      Logged in as <?php echo $_SESSION["user"]?>
    </p>
  <?php } else { ?>
      <a href="./login.php">Login</a>
  <?php } ?>
  <a href="#">Admin</a>
  <a href="#">View</a>
  <a href="./logout.php">Logout</a>
</div>
