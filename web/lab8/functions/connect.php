<?php
  function connect() {
    try {
      $con = new PDO("mysql:host=localhost;charset=utf8mb4", "cosmin", "cosmin");
      $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOExceptinon $pikatchu) {
      echo "Error connecting to database " . $pikachu->getMessage();
    }

    $con->query(" USE cosmin");

    try {
      $sql = "CREATE TABLE IF NOT EXISTS records (
        id INT PRIMARY KEY AUTO_INCREMENT,
        email VARCHAR(255) NOT NULL,
        title VARCHAR(1024) NOT NULL,
        comment VARCHAR(2048) NOT NULL,
        created_at TIMESTAMP
      )";
      $con->query($sql);
    } catch (PDOException $pikachu) {
      echo $sql . "<br>" . $pikachu->getMessage();
    }
    return $con;
  }
?>
