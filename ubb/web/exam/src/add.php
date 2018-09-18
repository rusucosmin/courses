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
  <h1>Add course</h1>
  <div id="content">
    <form action="./functions/add.php" method="post">
      <label>Course name</label>
      <input type="text" name="name" />
      <br />
      <label>Professor</label>
      <input type="text" name="professor" />
      <br />
      <label>Duration</label>
      <input type="number" name="duration" />
      <br />
      <label>Restrictions</label>
      <input type="text" name="restrictions" />
      <br />
      <input type="submit" value="Insert" />

    </form>
  </div>
  <?php include './layouts/footer.php'; ?>
</body>
</html>
