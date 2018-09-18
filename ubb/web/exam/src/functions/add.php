<?php
  session_start();

  $name = $_POST['name'];
  $professor = $_POST['professor'];
  $duration = $_POST['duration'];
  $restrictions = $_POST['restrictions'];

  include './connect.php';
  $con = connect();

  $stmt = $con->prepare("INSERT INTO Cursuri (denumire, profesor, durata) VALUES ('$name', '$professor', '$duration')");
  if(!$stmt->execute()) {
    $_SESSION['error'] = 'There was an error adding the course. Please check your values!';
    header("Location: ../index.php");
    return ;
  }
  $lastId = $con->lastInsertId();
  $rooms = explode(" ", $restrictions);
  $room = "";
  $stmt = $con->prepare("INSERT INTO Restrictii (idcurs, restrictii) VALUES ('$lastId', :room)");
  $stmt->bindParam(':room', $room);
  for($i = 0; $i < count($rooms); ++ $i) {
    $room = $rooms[$i];
    if(!$stmt->execute()) {
      $_SESSION['error'] = 'There was an error adding the course. Please check your values!';
      header("Location: ../index.php");
      return ;
    }
}
  header("Location: ../index.php");
?>
