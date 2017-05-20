<?php
  function get_car_by_id($id) {
      require_once 'config/database.php';

        try {
              $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
              $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

              $connect->query("USE " . $DB_NAME);

              $stmt = $connect->prepare("SELECT * FROM cars WHERE id=:id");
              $stmt->execute(array(":id" => $id));

              $val = $stmt->fetch();
              $stmt->closeCursor();

              return $val;
        }
        catch (PDOException $pikachu) {
            return "Error: " . $pikachu->getMessage();
        }
    }

    function get_all_cars($model) {
      require_once '../config/database.php';

      try {
              $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
              $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

              $connect->query("USE " . $DB_NAME);

              $asdf = "%" . $model . "%";
              $stmt = $connect->prepare("SELECT * FROM cars WHERE model LIKE :model");
              $stmt->execute(array(':model' => $asdf));

              error_log($asdf);

              $i = 0;
              $tab = null;
              while ($val = $stmt->fetch()) {
                $tab[$i]['id'] = $val['id'];
                $tab[$i]['model'] = $val['model'];
                $tab[$i]['fuel'] = $val['fuel'];
                $tab[$i]['capacity'] = $val['capacity'];
                $tab[$i]['fabrication_year'] = $val['fabrication_year'];

                $i++;
              }
              $stmt->closeCursor();

              return $tab;
        }
        catch (PDOException $pikachu) {
            return "Error: " . $pikachu->getMessage();
        }
    }
?>
