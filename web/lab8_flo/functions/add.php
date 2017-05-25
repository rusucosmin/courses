<?php

    function add_car($model, $capacity, $fuel, $year) {
      include_once '../config/database.php';

        try {
              $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
              $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

              $connect->query("USE " . $DB_NAME);

              $stmt = $connect->prepare("INSERT INTO cars (model, capacity, fuel, fabrication_year) VALUES (:model, :capacity, :fuel, :year)");
              $stmt->execute(array(":model" => $model, ":capacity" => $capacity, ":fuel" => $fuel, ":year" => $year));

        }
        catch (PDOException $pikachu) {
            $_SESSION['error'] = "Error: " . $pikachu->getMessage();
        }
    }

?>
