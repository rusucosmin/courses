<?php
  function update_car($id, $model, $capacity, $fuel, $year) {
      include_once '../config/database.php';

        try {
              $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
              $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

              $connect->query("USE " . $DB_NAME);

              $stmt = $connect->prepare("UPDATE cars SET model=:model, capacity=:capacity, fuel=:fuel, fabrication_year=:year WHERE id=:id");
              $stmt->execute(array(":model" => $model, ":capacity" => $capacity, ":fuel" => $fuel, ":year" => $year, ":id" => $id));

        }
        catch (PDOException $pikachu) {
            $_SESSION['error'] = "Error: " . $pikachu->getMessage();
        }
    }

?>