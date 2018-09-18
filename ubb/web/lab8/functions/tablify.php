<?php
function tablify($arr) {
  $table = "<table border='1'>
    <tr>
      <th>id</th>
      <th>eMail</th>
      <th>Title</th>
      <th>Comment</th>
      <th>Timestamp</th>
    </tr>
  ";
  foreach ($arr as $row) {
    $table = $table . "<tr>";
    $table =  $table ."<td>" . $row['id'] . "</td>";
    $table = $table . "<td>" . $row['email'] . "</td>";
    $table = $table . "<td>" . $row['title'] . "</td>";
    $table = $table . "<td>" . $row['comment'] . "</td>";
    $table = $table . "<td>" . $row['created_at'] . "</td>";
  }
  return $table;
}
?>

