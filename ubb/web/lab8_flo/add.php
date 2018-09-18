<?php
  session_start();
    include 'lib/includes.php';
  include 'partials/header.php';
?>


  <form method="post" action="forms/add.php">
    Model: <br> <input type="text" name="model"> <br><br>
        Engine capacity (in cmc): <br> <input type="text" name="capacity"> <br><br>
    Fuel: <br> <input type="text" name="fuel"> <br><br>
    Fabrication year: <br> <input type="text" name="fabrication_year"> <br><br>
    <input type="submit" name="submit" value="Add car">
  </form>
  <br>
    <span>
            <?php
            echo $_SESSION['error'];
            $_SESSION['error'] = null;
            ?>
    </span>


<?php
  include 'partials/footer.php';
?>
