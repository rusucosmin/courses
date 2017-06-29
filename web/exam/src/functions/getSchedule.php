<?php
  session_start();
  include 'connect.php';
  $day = $_GET['day'];

  $con = connect();
  $stmt = $con->prepare("SELECT Orar.zi, Orar.oraInceput, Orar.oraSfarsit, Cursuri.denumire as course, Sali.denumire as room FROM Orar
                        INNER JOIN Cursuri ON Cursuri.id=Orar.idcurs
                        INNER JOIN Sali ON Sali.id=Orar.idsala
                        WHERE Orar.zi = '$day'
                        ORDER BY Orar.oraInceput ASC");
  if(!$stmt->execute()) {
    die(json_encode(array()));
    return ;
  }
  die(json_encode($stmt->fetchAll()));
?>
