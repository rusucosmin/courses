<?php
  // Connect to the database server

  $connect = NULL;

  try {
    $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
    $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  }
  catch (PDOException $pikachu) {
    echo "DB connection failed: " . $pikachu->getMessage();
  }

  // Create the database

  try {
    $sql = "CREATE DATABASE IF NOT EXISTS " . $DB_NAME;
    $connect->query($sql);
  }
  catch (PDOException $pikachu) {
    echo "DB creation faild: " . $pikachu->getMessage();
  }

  $connect->query("USE " . $DB_NAME);

  // Create table cars

  try {
    $sql = "CREATE TABLE IF NOT EXISTS cars (
        id INT PRIMARY KEY AUTO_INCREMENT,
        model VARCHAR(255) NOT NULL,
        capacity INT NOT NULL,
        fuel VARCHAR(255) NOT NULL,
        fabrication_year INT NOT NULL,
        created_at TIMESTAMP
    )";
    $connect->query($sql);
  }
  catch (PDOException $pikachu) {
    echo $sql . "<br>" . $pikachu->getMessage();
  }
?>
