<?php
  session_start();
    // include 'lib/includes.php';
  include 'partials/header.php';
  include 'functions/read.php';

  $id = $_GET['id'];

  if ($id == "" || $id == null || !is_numeric($id)) {
    $_SESSION['error'] = "Car not found";
    header('Location: add.php');
  }

  $car = get_car_by_id($id);

  if ($car == null) {
    $_SESSION['error'] = "Car not found";
    header('Location: add.php');
  }

  $model = $car['model'];
  $capacity = $car['capacity'];
  $fuel = $car['fuel'];
  $year = $car['fabrication_year'];
?>


  <form method="post" action="forms/update.php">
    <input name="id" hidden value=<?php echo '"' . $id . '"'; ?>>
    Model: <br> <input type="text" name="model" value=<?php echo '"' . $model . '"'; ?>> <br><br>
        Engine capacity (in cmc): <br> <input type="text" name="capacity" value=<?php echo '"' . $capacity . '"'; ?>> <br><br>
    Fuel: <br> <input type="text" name="fuel" value=<?php echo '"' . $fuel . '"'; ?>> <br><br>
    Fabrication year: <br> <input type="text" name="fabrication_year" value=<?php echo '"' . $year . '"'; ?>> <br><br>
    <input type="submit" name="submit" value="Update car">
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
