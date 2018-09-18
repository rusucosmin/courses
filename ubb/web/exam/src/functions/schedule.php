<?php
  session_start();

  $idcurs = $_POST['idcurs'];
  $idsala = $_POST['idsala'];
  $zi = $_POST['zi'];
  $start = $_POST['hour'];
  $final = $start + $_POST['duration'];

  include './connect.php';
  $con = connect();

  $stmt = $con->prepare("INSERT INTO Orar (idcurs, idsala, zi, oraInceput, oraSfarsit)
                                  VALUES ('$idcurs', '$idsala', '$zi', '$start', '$final')");
  if(!$stmt->execute()) {
    $_SESSION['error'] = 'There was an error adding the course. Please check your values!';
    die("error");
    return ;
  }
  die("ok");
?>
