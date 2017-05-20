<?php
  include_once 'connect.php';

  $con = connect();

  try {
    $stmt = $con ->prepare("SELECT * FROM records WHERE INSTR(email, :email) > 0 AND INSTR(title, :title) > 0");
    $res = [];
    $stmt->execute(array(":email" => $_GET["email"], ":title" => $_GET["title"]));
    $res = $stmt->fetchAll();
    exit(json_encode($res));
  } catch (PDOException $pikachu) {
    echo "Eroare: " . $pikachu->getMessage();
    $_SESSION['error'] = "Error: " . $pikachu->getMessage();
    exit($pikachu->getMessage());
  }
?>
