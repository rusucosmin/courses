<?php
  session_start();
  if(!array_key_exists("user", $_SESSION)) {
    $_SESSION["error"] = "Please login first!";
    header("Location: ./index.php");
    return ;
  }
?>

<!DOCTYPE html>
<html>
<head>
  <?php include './layouts/scripts.php'; ?>
  <script>
    var user = "<?php echo $_SESSION["user"] ?>";
    $(document).ready(function() {
      setInterval(function () {
        $.get("./functions/sent.php", {"user": user}, function(data) {
          $("#chat").empty();
          var arr = JSON.parse(data);
          for(var i = 0; i < arr.length; ++ i) {
            $("#chat").append(createMessage(arr[i]));
          }
        });
      }, 1000);
      function createMessage(obj) {
        var li = $("<li></li>");
        li.append(createItem("Sender", "sender", obj));
        li.append(createItem("Message", "text", obj));
        li.append(createItem("Receivers", "receivers", obj));
        li.append(createItem("Views", "views", obj));
        li.append($("<button>Delete</button>")
                    .addClass("deleteBtn")
                    .attr("id", obj.id));
        return li;
      }
      function createItem(dt, dd, obj) {
        var dl = $("<dl></dl>");
        dl.append($("<dt>" + dt + "</dt>"));
        dl.append($("<dd>" + obj[dd] + "</dd>"));
        return dl;
      }
    });
    $(document).on('click', '.deleteBtn', function() {
      console.log("deletbnt");
      console.log($(this).attr("id"));
      $(this).parent().fadeOut();
      $.get("./functions/delete.php", {id: $(this).attr("id")}, function(data) {
          loadData();
      });
    });
  </script>
</head>
<body>
  <h1>Chat</h1>
  <?php include './layouts/header.php'; ?>
  <?php
    if(array_key_exists("message_sent", $_SESSION)) {
        echo $_SESSION["message_sent"];
        unset($_SESSION["message_sent"]);
    }
  ?>
  <div id="content">
    <ol id="chat">
    </ol>
  </div>
  <?php include './layouts/footer.php'; ?>
</body>
</html>
