<!DOCTYPE html>
<html>
  <?php include 'layouts/scripts.php' ?>
  <script>
    $(document).ready(function() {
      filter("", ""); // get all
      var xmlHttp;
      $("#filterBtn").click(function() {
        var _title = $("#titleInput").val();
        var _email = $("#emailInput").val();
        filter(_title, _email);
      });

      function filter(_title, _email) {
        var url="functions/filter.php";
        url = url + "?title=" + _title;
        url = url + "&email=" + _email;
        xmlHttp = getXmlHttpObject();
        xmlHttp.onreadystatechange=stateChanged;
        xmlHttp.open("GET", url, true);
        xmlHttp.send(null);
      }

      function stateChanged() {
        if(xmlHttp.readyState == 4) {
          var arr = JSON.parse(xmlHttp.responseText);
          $("#result tbody").empty();
          for(var i = 0; i < arr.length; ++ i) {
            var row = "<tr>";
            var row = row + "<td>" + arr[i]["id"] + "</td>";
            var row = row + "<td>" + arr[i]["email"] + "</td>";
            var row = row + "<td>" + arr[i]["title"] + "</td>";
            var row = row + "<td>" + arr[i]["comment"] + "</td>";
            var row = row + "<td>" + arr[i]["timestamp"] + "</td>";
            var row = row + "</tr>";
            $("#result tbody").append(row);
          }
        }
      }

      function getXmlHttpObject() {
        if(window.XMLHttpRequest)
          return new XMLHttpRequest();
        if(window.ActiveXObject)
          return new ActiveXObject("Microsoft.XMLHTTP");
        return null;
      }
    });
  </script>
  <body>
    <?php include 'layouts/header.php' ?>
    <div id="content">
      <h2>Admin control panel</h2>
      <h3>Filter</h3>
      <label>e-mail</label>
      <input id="emailInput" type="text"/>
      <label>title</label>
      <input id="titleInput" type="text"/>
      <input id="filterBtn" type="submit"/>
      <h3>Results</h3>
      <table id="result" border='1'>
        <thead>
          <tr>
            <th>id</th>
            <th>eMail</th>
            <th>Title</th>
            <th>Comment</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
    </div>
    <?php include 'layouts/footer.php' ?>
  </body>
</html>
