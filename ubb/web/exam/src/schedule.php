<?php
  session_start();
?>

<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
  <style>
  table {
    border-collapse: collapse;
  }
  td, th {
    border: 1px solid #dddddd;
  }
  #content {
    font-size: 20px;
  }
  </style>
  <script>
    var courses;
    var rooms;
    var auxRooms;
    function getPlanned() {
      auxRooms = jQuery.extend(true, {}, rooms);
      var data = {
        "day": $("#day").val(),
        "hour": $("#startHour").val(),
        "duration": courses[$("#ddcourses").val()].durata
      };
      console.log($("#ddcourses").val());
      console.log(data);
      $.get("./functions/getPlanned.php", data, function(data) {
        var arr = JSON.parse(data);
        for(var i = 0; i < arr.length; ++ i) {
          auxRooms[arr[i].idsala]['planned'] = true;
        }
        getRestricted();
      });
    }
    function getCourses() {
      courses = {};
      $.get("./functions/getCourses.php", function(data) {
        var arr = JSON.parse(data);
        $("#ddcourses").empty();
        for(var i = 0; i < arr.length; ++ i) {
          courses[arr[i].id] = arr[i];
          $("#ddcourses").append(
            $("<option></option>").attr("value", arr[i].id).text(arr[i].denumire).attr("duration", arr[i].duration)
          );
        }
        console.log(courses);
      });
    }

    function getRooms() {
        rooms = {};
        $.get("./functions/getRooms.php", function(data) {
          var arr = JSON.parse(data);
          for(var i = 0; i < arr.length; ++ i) {
            rooms[arr[i].id] = arr[i];
          }
          console.log(rooms);
        });
      }
      function getRestricted() {
        var data = {
          "id": $("#ddcourses").val()
        }
        $.get("./functions/getRestrictions.php", data, function(data) {
          var arr = JSON.parse(data);
          console.log(arr);
          for(var i = 0; i < arr.length; ++ i) {
            auxRooms[arr[i].idsala]['restricted'] = true;
          }
          showTable();
        });
      }
      function showTable() {
        $("#schedule").empty();
        var roomIds = Object.keys(auxRooms);
        for(var i = 0; i < roomIds.length; ++ i) {
          var room = auxRooms[roomIds[i]];
          if(room['restricted'] == true) {
            $("#schedule").append($("<tr><td></td></tr>")
              .text(room.denumire)
              .css("background-color", "red")
              .attr("id", room.id)
              .addClass("room"));
          }
          else if(room['planned'] == true) {
            $("#schedule").append($("<tr><td></td></tr>")
              .text(room.denumire)
              .css("background-color", "orange")
              .attr("id", room.id)
              .addClass("room"));
          } else {
            $("#schedule").append($("<tr><td></td></tr>")
              .text(room.denumire)
              .css("background-color", "green")
              .attr("id", room.id)
              .addClass("room"));
          }
        }
        $("#schedule").fadeIn();
      }
    $(document).ready(function() {
      getCourses();
      getRooms();
      $("#ddcourses").click(function() {
        console.log($("#ddcourses").val());
      });
      $("#check").click(function() {
        console.log('check clicked');
        getPlanned();
      });
    });
    $(document).on('click', '.room', function() {
      console.log("roomClick");
      if($(this).css('background-color') !== "rgb(0, 128, 0)") {
        alert("Please click green! You sneaky");
        return ;
      }
      var data = {
        "idcurs": $("#ddcourses").val(),
        "idsala": $(this).attr("id"),
        "zi": $("#day").val(),
        "hour": $("#startHour").val(),
        "duration": courses[$("#ddcourses").val()].durata
      };
      console.log(data);
      $.post("./functions/schedule.php", data, function(data) {
        if(data === "error")  {
          window.location.replace("./index.php")
          return ;
        }
        else if(data == "ok") {
          getPlanned();
        }
        console.log(data);
      });
    });
  </script>
</head>
<body>
  <?php include './layouts/header.php'; ?>
  <h1>Schedule a course</h1>
  <div id="content">
    <label>Course</label>
    <select type="text" name="course" id="ddcourses">
    </select>
    <br />
    <label>Day</label>
    <select type="text" name="day" id="day">
      <option>
        Luni
      </option>
      <option>
        Marti
      </option>
      <option>
        Miercuri
      </option>
      <option>
          Joi
      </option>
      <option>
          Vineri
      </option>
    </select>
    <br />
    <label>Starting Hour</label>
    <input type="number" name="startHour" id="startHour" />
    <br />
    <input type="submit" value="Check" id="check" />
    <table id = "schedule" hidden>
      <tr>
        <th>
          Room Name
        </th>
      </tr>
    </table>
  </div>
  <?php include './layouts/footer.php'; ?>
</body>
</html>
