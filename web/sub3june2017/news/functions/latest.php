<?php
  include 'connect.php';

  $con = connect();
  $query = $con->query("SELECT * FROM News ORDER BY Date DESC LIMIT 5");
  $res = $query->fetchAll();

  $json = array();
  $json["news"] = $res;

  exit(json_encode($json));
?>
