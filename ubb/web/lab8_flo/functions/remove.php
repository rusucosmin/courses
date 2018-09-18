<?php
	function remove_car($id) {
      include_once '../config/database.php';

        try {
              $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
              $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

              $connect->query("USE " . $DB_NAME);

              $stmt = $connect->prepare("DELETE FROM cars WHERE id=:id");
              $stmt->execute(array(":id" => $id));

        }
        catch (PDOException $pikachu) {
            $_SESSION['error'] = "Error: " . $pikachu->getMessage();
        }
    }
?>