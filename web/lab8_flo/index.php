<?php
  session_start();
  include 'lib/includes.php';
  include 'partials/header.php';
?>

<button onclick="addCar()">
  Add a car
</button>

<input id="queryInput" type="text" value=""/>
<button onclick="getCars()">
  Filter model
</button>

<br>

<table id="carsTable">

</table>

<script>
  $('document').ready(function() {
    getCars();
  });

  function getCars() {

    var query = $('#queryInput').val();
    $('#carsTable').empty();
    $.ajax({
      url: "api/cars.php?query=" + query,
      success: function(result) {
        var obj = jQuery.parseJSON(result);
        $.each( obj, function( key, value ) {
          var id = value['id'];
            var model = value['model'];
            var capacity = value['capacity'];
            var fuel = value['fuel'];
            var year = value['fabrication_year'];
            $('#carsTable').append('<tr class="row"> <div class="cell"> <td><input class="theInput" type="text" value="' + model + '" readonly></td><td><input class="theInput" type="text" value="' + capacity + '" readonly></td><td><input class="theInput" type="text" value="' + fuel + '" readonly></td><td><input class="theInput" type="text" value="' + year + '" readonly></td></div><td class="special"><button type="button" class="update" onclick="updateCar(' + id + ')">Update</button></td><td class="special"><button type="button" class="delete" onclick="deleteCar(' + id + ')">Delete</button></td></tr>');
        });
        
      }
    });
  }

  function addCar() {
    window.location = "add.php";
  }

  function deleteCar(id) {
    console.log("I should delete the car with id: " + id);
  }

  function updateCar(id) {
    window.location = "update.php?id=" + id;
  }
</script>

<?php

  include 'partials/footer.php';
?>
