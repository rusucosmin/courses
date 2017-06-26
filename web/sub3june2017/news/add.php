<?php
  session_start();
?>
<!DOCTYPE html>
<html>
  <head>
    <script src="scripts/jquery-3.2.1.js"></script>
    <script>
    $(document).ready(function() {
      $.ajaxSetup({ cache: false });
      $('#add-more').click(function() {
        console.log('add-more');
        $('#news-form').append(
          "<hr />" +
          "<label>Title</label>" +
          "<input name='titles[]' type='text' />" +
          "<br />" +
          "<label>Description</label>" +
          "<input name='descriptions[]' type='text' />" +
          "<br />"
        );
      });
      loadData();
      function loadData() {
        $.get("./functions/get.php", function(data) {
          console.log("got all");
          var obj = JSON.parse(data).news;
          var div = $("#content");
          div.empty();
          for(var i = 0; i < obj.length; ++ i) {
            if (obj[i].UserID != 1)
              continue;
            div.append("<p>" + obj[i].Title + "</p>");
            div.append("<p>" + obj[i].Description + "</p>");
            div.append("<p>" + obj[i].UserID + "</p>");
            var btn = $("<button>Delete</button>")
            btn.attr('id', obj[i].ID);
            btn.click(function() {
              console.log("clicked: " + $(this).attr('id'));
              $.get("./functions/delete.php", {id: $(this).attr('id')}, function(data) {
                console.log(data);
                loadData();
              });
            });
            div.append(btn);
          }
        });
      }
    });
    </script>
  </head>
  <body>
    <?php echo $_SESSION['user_id'] ?>
    <form id="news-form" action="./forms/add.php" method="post">
      <input value="Insert" type="submit" />
      <hr />
      <label>Title</label>
      <input name="titles[]" type="text" />
      <br />
      <label>Description</label>
      <input name="descriptions[]" type="text" />
      <br />
    </form>
    <input id="add-more" value="Add more stories" type="submit" />
    <form action="./forms/logout.php" method="post">
      <input type="submit" value="Logout" />
    </form>
    <p>
      Your stories
    </p>
    <div id="content">
    </div>
  </body>
</html>
