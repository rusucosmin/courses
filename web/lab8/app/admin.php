<!DOCTYPE html>
<html>
  <?php include '../layouts/scripts.php' ?>
  <script>
    $(document).ready(function() {
      filter("", "", 1); // get all
      $("#filterBtn").click(function() { 
        console.log("clicked on filter");
        var _title = $("#titleInput").val();
        var _email = $("#emailInput").val();
        filter(_title, _email, 1);
      });

      $("#titleInput").on("input propertychange paste", function() {
        console.log("changed title");
        var _title = $("#titleInput").val();
        var _email = $("#emailInput").val();
        filter(_title, _email, 1);
      });

      $("#emailInput").on("input propertychange paste", function() {
        console.log("changed email");
        var _title = $("#titleInput").val();
        var _email = $("#emailInput").val();
        filter(_title, _email, 1);
      });

      function filter(_title, _email, _page) {
        console.log("filter: " + _title + " " + _email);
        var url="../functions/filter.php";
        url = url + "?title=" + _title;
        url = url + "&email=" + _email;
        url = url + "&page=" + _page;
        $.get(url, function(data, status) {
          console.log(data);
          filterStateChanged(data);
        });
      }

      function callDelete(id) {
        var url="../api/delete.php?id=" + id;
        $.get(url, function(data, status) {
          deleteStateChanged(data);
        });
      }

      function deleteStateChanged(response) {
        var res = JSON.parse(response);
        if(res["response"] == "ok") {
          console.log("ok");
        }
        else {
          console.log("error deleting: ");
        }
      }

      function filterStateChanged(res) {
        var res = JSON.parse(res);
        var arr = res["records"];
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
            location.href = '/lab8/app/edit.php?id=' + $(this).attr('id');
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
        $("#paginate").empty();
        for(var i = 0; i < res["total_pages"]; ++ i) {
          var pageBtn = $("<button></button>");
          pageBtn.text((i + 1));
          pageBtn.attr("id", (i + 1));
          pageBtn.click(function () {
            var _title = $("#titleInput").val();
            var _email = $("#emailInput").val();
            filter(_title, _email, $(this).attr("id"));
          });
          $("#paginate").append(pageBtn);
        }
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
      <div id="paginate" align="center">
      </div>
    </div>
    <?php include '../layouts/footer.php' ?>
  </body>
</html>
