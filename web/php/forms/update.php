<?php
    session_start();

    include_once '../functions/update.php';
    include_once '../lib/utils.php';

    $id = test_input($_POST["id"]);
    $model = test_input($_POST["model"]);
    $capacity = test_input($_POST["capacity"]);
    $fuel = test_input($_POST["fuel"]);
    $fabrication_year = test_input($_POST["fabrication_year"]);

    if ($model == "" || $model == null || $capacity == "" || $capacity == null || $fuel == "" || $fuel == null || $fabrication_year == "" || $fabrication_year == null) {
        $_SESSION['error'] .= "Update car failed. All fields must be filled.";
        header("Location: ../update.php?id=" . $id);
    } else {

        update_car($id, $model, $capacity, $fuel, $fabrication_year);

        header("Location: ../index.php");
    }
?>