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
      $user = $_POST['user'];
      $password = $_POST['password'];

      /// todo: connect to db and redirect
      $con = connect();
      $q = $con->query("SELECT * FROM Users where User = '".$user."' and Password = '".$password."'");

      if($q->rowCount() > 0) {
        $uObj = $q->fetch(PDO::FETCH_OBJ);
        echo "Logged in as ";
        $_SESSION['user'] = $uObj->User;
        $_SESSION['user_id'] = $uObj->ID;
        echo $_SESSION['user_id'];
        $_SESSION['user_role'] = $uObj->Role;
        $_SESSION['user_password'] = $uObj->Password;
      } else {
        echo "Failed to login";
        echo $user;
        echo $password;
      }
    ?>
  </body>
  <input type="submit" value="Back" onclick="history.go(-1)"/>
</html>
