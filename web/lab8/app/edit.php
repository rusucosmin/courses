<!DOCTYPE html>
<html>
  <?php include '../layouts/scripts.php' ?>
  <?php
    session_start();
    include_once '../functions/connect.php';

    $con = connect();
    $id = isset($_GET['id']) ? $_GET['id'] : '';

    if($id == "" || $id == null || !is_numeric($id)) {
      $_SESSION['error'] = "Record not found";
    }

    try {
      $stmt = $con->prepare("SELECT * FROM records WHERE id = :id");
      $stmt->execute(array(":id" => $id));
      if($stmt->rowCount() == 0) {
        $_SESSION['error'] = "Record not found.";
        $id = null;
      }
      $record = $stmt->fetch();
      $id = $record['id'];
      $email = $record['email'];
      $title = $record['title'];
      $comment = $record['comment'];
    } catch(PDOException $pikachu) {
      $_SESSION['error'] = "Record not found: " . $pikachu->getMessage();
    }
  ?>
  <body>
    <?php include '../layouts/header.php' ?>
    <div id="content">
      <h2>Edit record</h2>
      <h3>Update</h3>
      <form method="post" action="../forms/update.php" <?php if(!$id) echo "hidden"?>>
        <input name="id" hidden value=<?php echo '"' . $id . '"' ?>>
        <label>eMail: </label>
        <input name="email" type="email" value=<?php echo '"' . $email . '"'?>>
        <label>Title: </label>
        <input name="title" type="text" value=<?php echo '"' . $title . '"'?>>
        <label>Comment: </label>
        <input name="comment" type="text" value=<?php echo '"' . $comment . '"'?>>
        <input type="submit" name="submit" value="Update">
      </form>
      <span>
        <?php
          echo $_SESSION['error'];
          $_SESSION['error'] = null;
        ?>
      </span>
    </div>
    <?php include '../layouts/footer.php' ?>
  </body>
</html>
