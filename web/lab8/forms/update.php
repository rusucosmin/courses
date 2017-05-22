<!DOCTYPE html>
<html>
  <?php include '../layouts/scripts.php'?>
  <?php
    include '../functions/connect.php';

    $id = $_POST['id'];
    $email = $_POST['email'];
    $title = $_POST['title'];
    $comment = $_POST['comment'];

    $con = connect();

    try {
      $stmt = $con->prepare("UPDATE records SET email = :email, title = :title, comment = :comment WHERE id = :id");
      $stmt->execute(array(":id" => $id, ":email" => $email, ":title" => $title, ":comment" => $comment));
    } catch(PDOException $pikachu) {
      $_SESSION["error"] = "Erorr: " . $pikachu.getMessage();
      $_SESSION["error"] = null;
    }
  ?>
  <body>
    <?php include '../layouts/header.php'; ?>
    <div id="content">
      <h2>Updated</h2>
      <h3>Successfully updated</h3>
      <p><?php echo "eMail: " . $_POST["email"]?></p>
      <p><?php echo "title: " . $_POST["title"]?></p>
      <p><?php echo "comment: " . $_POST["comment"]?></p>
    </div>
    <?php include '../layouts/footer.php'; ?>
  </body>
</html>
