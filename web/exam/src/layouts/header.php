<div id="header">
  <p>
    <?php
      if(array_key_exists("error", $_SESSION)) {
          echo $_SESSION["error"];
          unset($_SESSION["error"]);
      }
    ?>
  </p>
  <a href="./index.php">Home</a>
  <a href="./add.php">Add course</a>
  <a href="./schedule.php">Schedule course</a>
  <a href="./show.php">Show Schedule</a>
  <hr />
</div>
