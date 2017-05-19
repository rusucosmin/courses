<!DOCTYPE html>
<html>
  <?php include 'layouts/scripts.php' ?>
  <body>
    <?php include 'layouts/header.php' ?>
    <div id="content">
      <h2>Admin control panel</h2>
      <?php
        include_once 'functions/connect.php';
        $con = connect();
        echo "<table border='1'>
          <tr>
            <th>id</th>
            <th>eMail</th>
            <th>Title</th>
            <th>Comment</th>
            <th>Timestamp</th>
          </tr>
        ";
        $sql = "SELECT * FROM records";
        foreach ($con->query($sql) as $row) {
          echo "<tr>";
          echo "<td>" . $row['id'] . "</td>";
          echo "<td>" . $row['email'] . "</td>";
          echo "<td>" . $row['title'] . "</td>";
          echo "<td>" . $row['comment'] . "</td>";
          echo "<td>" . $row['created_at'] . "</td>";
        }
      ?>
    </div>
    <?php include 'layouts/footer.php' ?>
  </body>
</html>
