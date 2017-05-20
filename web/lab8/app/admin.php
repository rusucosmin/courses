<!DOCTYPE html>
<html>
  <?php include '../layouts/scripts.php' ?>
  <script>
    $(document).ready(function() {
      filter("", ""); // get all
      var filterXmlHttp;
      var deleteXmlHttp;
      $("#filterBtn").click(function() {
        var _title = $("#titleInput").val();
        var _email = $("#emailInput").val();
        filter(_title, _email);
      });

      $(".editBtn").click(function() {
        console.log("clicked");
      });

      $(".deleteBtn").bind("click", function() {
        console.log("deleteBtn clicked");
      });

      function filter(_title, _email) {
        var url="../functions/filter.php";
        url = url + "?title=" + _title;
        url = url + "&email=" + _email;
        filterXmlHttp = getXmlHttpObject();
        filterXmlHttp.onreadystatechange=filterStateChanged;
        filterXmlHttp.open("GET", url, true);
        filterXmlHttp.send(null);
      }

      function callDelete(id) {
        var url="../api/delete.php?id=" + id;
        deleteXmlHttp = getXmlHttpObject();
        deleteXmlHttp.onreadystatechange=deleteStateChanged;
        deleteXmlHttp.open("GET", url, true);
        deleteXmlHttp.send(null);
      }

      function deleteStateChanged() {
        if(deleteXmlHttp.readyState == 4) {
          var res = JSON.parse(deleteXmlHttp.responseText);
          if(res["response"] == "ok") {
            console.log("ok");
          }
          else {
            console.log("error deleting: ");
          }
        }
      }

      function filterStateChanged() {
        if(filterXmlHttp.readyState == 4) {
          var arr = JSON.parse(filterXmlHttp.responseText);
          $("#result tbody").empty();
          for(var i = 0; i < arr.length; ++ i) {
            var row = $("<tr></tr>");
            var rowid = $("<td></td>").text(arr[i]["id"]);
            var rowemail = $("<td></td>").text(arr[i]["email"]);
            var rowtitle = $("<td></td>").text(arr[i]["title"]);
            var rowcomment = $("<td></td>").text(arr[i]["comment"]);
            var rowcreated = $("<td></td>").text(arr[i]["created_at"]);
            var rowedit = $("<button>Edit</button>");
            var rowdelete = $("<button>Delete</button>");
            rowdelete.attr("id", arr[i]["id"]);
            rowdelete.click(function(){
              console.log("clicked: " + $(this).attr("id"));
              callDelete($(this).attr("id"));
              $(this).parent().remove();
            });
            rowedit.attr("id", arr[i]["id"]);
            rowedit.click(function() {
              console.log("clicked edit" + $(this).attr("id"));
            });
            row.append(rowid);
            row.append(rowemail);
            row.append(rowtitle);
            row.append(rowcomment);
            row.append(rowcreated);
            row.append(rowedit);
            row.append(rowdelete);
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
    <?php include '../layouts/header.php' ?>
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
    <?php include '../layouts/footer.php' ?>
  </body>
</html>
