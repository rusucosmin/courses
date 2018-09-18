<?php
  session_start();
?>
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <?php
      include '../functions/connect.php';
      $titles = $_POST['titles'];
      $descriptions = $_POST['descriptions'];

      print_r($titles);
      print_r($descriptions);

      $con = connect();

      $stmt = $con->prepare("INSERT INTO News (Title, Description, UserID) VALUES (:title, :description, :id)");

      $stmt->bindParam(':id', $_SESSION['user_id']);
      $stmt->bindParam(':title', $title);
      $stmt->bindParam(':description', $description);

      for($i = 0; $i < count($titles); $i ++) {
        $title = $titles[$i];
        $description = $descriptions[$i];
        $stmt->execute();
      }
    ?>
  </body>
  <input type="submit" value="Back" onclick="history.go(-1)"/>
</html>
