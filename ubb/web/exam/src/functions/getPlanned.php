<?php
  session_start();
  include 'connect.php';

  $day = $_GET['day'];
  $hour = $_GET['hour'];
  $duration = $_GET['duration'];
  $final = $hour + $duration;

  $con = connect();

  // a0 <= b1 && b0 <= a1;
  // [a0, a1] AND
  // [b0, b1]
  // [oraInceput, oraSfarsit],
  // [hour, final]
  $stmt = $con->prepare("SELECT * FROM Orar
                        WHERE zi = '$day'
                        AND (oraInceput < '$final'
                        AND '$hour' < oraSfarsit)");
  if(!$stmt->execute()) {
    die(json_encode(array()));
    return ;
  }
  die(json_encode($stmt->fetchAll()));
?>
