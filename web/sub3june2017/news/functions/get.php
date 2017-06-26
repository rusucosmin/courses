<?php
  include 'connect.php';

  $con = connect();
  $query = $con->query("SELECT * FROM News");
  $res = $query->fetchAll();

  $json = array();
  $json["news"] = $res;
  
  exit(json_encode($json));
?>
