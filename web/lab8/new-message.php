<!DOCTYPE html>

<html>
  <?php include 'layouts/scripts.php'; ?>
  <body>
    <?php include 'layouts/header.php'; ?>
    <div id="content">
      <h2>Thank you for your message!</h2>
      <p><?php echo $_POST["email"]?></p>
      <p><?php echo $_POST["title"]?></p>
      <p><?php echo $_POST["comment"]?></p>
    </div>
    <?php include 'layouts/footer.php'; ?>
  </body>
</html>
