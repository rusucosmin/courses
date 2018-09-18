<?php
  include_once 'connect.php';

  function getFilterCount($email, $title) {
    $con = connect();
    try {
      $count_all = $con->prepare("SELECT COUNT(*) FROM records WHERE INSTR(email, $email) > 0 AND INSTR(title, $title) > 0");
      $get_total_row = $count_all->fetch();
    }
    catch (PDOException $e) {
      die("Error: " . e.getMessage());
    }
    return $get_total_row[0];
  }
?>
