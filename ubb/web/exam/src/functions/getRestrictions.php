<?php
  session_start();
  include 'connect.php';
  $id = $_GET['id'];

  $con = connect();
//  $stmt = $con->prepare("SELECT * FROM Restrictii WHERE idcurs = '$id' JOIN ");
  $stmt = $con->prepare("SELECT Restrictii.idcurs, Restrictii.restrictii, Sali.id as idsala, Sali.denumire
                        FROM Restrictii
                        INNER JOIN Sali ON Restrictii.restrictii=Sali.denumire
                        WHERE idcurs='$id'
                        ");
  if(!$stmt->execute()) {
    die(json_encode(array()));
    return ;
  }
  die(json_encode($stmt->fetchAll()));
?>
