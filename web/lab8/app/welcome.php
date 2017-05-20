<!DOCTYPE html>

<html>
  <?php include 'layouts/scripts.php'; ?>
  <body>
    <?php include 'layouts/header.php'; ?>
    <div id="content">
      <h2>Welcome! You can leave us a message.</h2>
      <form action="forms/new.php" method="post">
        <label>
          e-Mail:
        </label>
        <input type="email" name="email"/>
        <br>
        <label>
          Title:
        </label>
        <input type="text" name="title"/>
        <br>
        <label>
          Comment
        </label>
        <input type="text" name="comment"/>
        <br>
        <input type="submit" />
      </form>
    </div>
    <?php include 'layouts/footer.php'; ?>
  </body>
</html>
