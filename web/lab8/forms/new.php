<!DOCTYPE html>

<html>
  <?php include '../layouts/scripts.php'; ?>
  <body>
    <?php include '../layouts/header.php'; ?>
    <div id="content">
      <h2>Thank you for your message!</h2>
      <p><?php echo "eMail: " . $_POST["email"]?></p>
      <p><?php echo "title: " . $_POST["title"]?></p>
      <p><?php echo "comment: " . $_POST["comment"]?></p>
      <?php
        include_once '../functions/connect.php';
        $con = connect();
        try {
          $stmt = $con->prepare("INSERT INTO records (email, title, comment) VALUES (:email, :title, :comment)");
          $stmt->execute(array(":email" => $_POST["email"],
                               ":title" => $_POST["title"],
                               ":comment" => $_POST["comment"]));
        } catch (PDOException $pikachu) {
          echo "Erroare" . $pikachu->getMessage();
          $_SESSION['error'] = "Error: " . $pikachu->getMessage();
        }
      ?>
    </div>
    <?php include '../layouts/footer.php'; ?>
  </body>
</html>
