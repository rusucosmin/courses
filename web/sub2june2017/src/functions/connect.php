<?php
  function connect() {
    try {
      $con = new PDO("mysql:host=localhost;charset=utf8mb4", "exam", "exam");
      $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOExceptinon $pikatchu) {
      echo "Error connecting to database " . $pikachu->getMessage();
    }

    /// database exam
    $con->query("USE exam");

    return $con;
  }
?>
