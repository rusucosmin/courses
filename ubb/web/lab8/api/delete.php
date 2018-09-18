<?php
  include_once '../functions/connect.php';

  $con = connect();

  try {
    $stmt = $con->prepare("DELETE FROM records WHERE id = :id");
    $stmt->execute(array(":id" => $_GET["id"]));
    $res = array("response" => "ok");
    $res["row_count"] = $stmt->rowCount();
    exit(json_encode($res));
  } catch(PDOException $pikachu) {
    echo "Error: " . $pikachu->getMessage();
    $_SESSION['error'] = "Error: " . $pikachu->getMessage();
    $res = array("response" => "error");
    exit(json_encode($res));
  }
?>
