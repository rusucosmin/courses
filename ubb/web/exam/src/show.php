<?php
  session_start();
?>

<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
  <style>
  table{
  }
  </style>
  <script>
    function getDay(day) {
      $.get("./functions/getSchedule.php", {day: day}, function(data) {
        console.log("got data for:" + day);
        var tbl = $("#" + day);
        /*
        var arr = JSON.parse(data);
        for(var i = 0; i < arr.length; ++ i) {
          var o = arr[i];
          tbl.append($("<tr></tr>"))
                      .append($("<td></td>"))
                                          .html(beauty(o))
        }
        */
        JSON.parse(data).forEach((o) => tbl.append($("<tr></tr>")
                                                    .append($("<td></td>")
                                                        .html(beauty(o))
                                                      )
                                                  ));
      });
    }
    function beauty(o) {
      return o.zi + " " + o.course + " " + o.room + " " + o.oraInceput + " " + o.oraSfarsit;
    }
    $(document).ready(function() {
      getDay("luni");
      getDay("marti");
      getDay("miercuri");
      getDay("joi");
      getDay("vineri");
    });
  </script>
</head>
<body>
  <?php include './layouts/header.php'; ?>
  <h1>Schedule</h1>
  <div id="content">
    <table id="luni">
      <tr>
        <th>Luni</th>
      </tr>
    </table>
    <table id="marti">
      <tr>
        <th>Marti</th>
      </tr>
    </table>
    <table id="miercuri">
      <tr>
        <th>Miercuri</th>
      </tr>
    </table>
    <table id="joi">
      <tr>
        <th>Joi</th>
      </tr>
    </table>
    <table id="vineri">
      <tr>
        <th>Vineri</th>
      </tr>
    </table>
    <br />
  </div>
  <?php include './layouts/footer.php'; ?>
</body>
</html>
