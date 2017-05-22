<?php
  include_once 'connect.php';
  include_once 'filter_size.php';

  $con = connect();

  try {
    if(isset($_GET["page"])) {
      $page_number = filter_var($_GET["page"], FILTER_SANITIZE_NUMBER_INT, FILTER_FLAG_STRIP_HIGH);
    }
    else {
      $page_number = 1;
    }
    $item_per_page = 2;

    $count_all = $con->prepare("SELECT COUNT(*) FROM records WHERE INSTR(email, :email) > 0 AND INSTR(title, :title) > 0");
    $count_all->execute(array(":email" => $_GET["email"],
                              ":title" => $_GET["title"]));

    $get_total_row = $count_all->fetch();
    $total_pages = ceil($get_total_row[0] / $item_per_page);
    $page_position = (($page_number - 1) * $item_per_page);

    $stmt = $con->prepare("SELECT * FROM records WHERE INSTR(email, :email) > 0 AND INSTR(title, :title) > 0 ORDER BY id ASC LIMIT $page_position, $item_per_page");
    $stmt->execute(array(":email" => $_GET["email"],
                         ":title" => $_GET["title"]));
    $res = $stmt->fetchAll();
    $json = array();
    $json["records"] = $res;
    $json["total_pages"] = $total_pages;
    $json["page_position"] = $page_position;
    $json["item_per_page"] = $item_per_page;
    exit(json_encode($json));
  } catch (PDOException $pikachu) {
    echo "Eroare: " . $pikachu->getMessage();
    $_SESSION['error'] = "Error: " . $pikachu->getMessage();
    exit($pikachu->getMessage());
  }
?>
