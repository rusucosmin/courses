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
      var latest = null;
      var lastId = null;
      var ind
      function arraysEqual(a, b) {
        if (a === b) return true;
        if (a == null || b == null) return false;
        if (a.length != b.length) return false;

        // If you don't care about the order of the elements inside
        // the array, you should sort both arrays here.

        for (var i = 0; i < a.length; ++i) {
          if (!isEquivalent(a[i], b[i])) return false;
        }
        return true;
      }
      function isEquivalent(a, b) {
        // Create arrays of property names
        var aProps = Object.getOwnPropertyNames(a);
        var bProps = Object.getOwnPropertyNames(b);

        // If number of properties is different,
        // objects are not equivalent
        if (aProps.length != bProps.length) {
            return false;
        }

        for (var i = 0; i < aProps.length; i++) {
            var propName = aProps[i];

            // If values of same property are not equal,
            // objects are not equivalent
            if (a[propName] !== b[propName]) {
                return false;
            }
        }

        // If we made it this far, objects
        // are considered equivalent
        return true;
      }

      function showNews(obj) {
        $("#title").fadeOut(function() {
          $(this).text(obj.Title).fadeIn();
        });
        $("#description").fadeOut(function() {
          $(this).text(obj.Description).fadeIn();
        });
        $("#author").fadeOut(function() {
          $(this).text(obj.UserID).fadeIn();
        });
      }
      setInterval(function() {
        $.get("./functions/latest.php", function(data) {
          console.log("requesting");
          var obj = JSON.parse(data);
          console.log(obj.news);
          console.log(latest);
          if(latest != null && arraysEqual(latest, obj.news))
            return ;
          if (lastId != null)
            clearInterval(lastId);
          console.log("stiri noi");
          showSpan();
          latest = obj.news;
          ind = 0;
          lastId = setInterval(function() {
            showNews(latest[ind]);
            ind = (ind + 1) % 5;
          }, 1500)
        });
      }, 2500);
      function showSpan() {
        var span = $('<span />').html("A aparut o stire noua!");
        $("#content").append(span);
        setTimeout(function() {
          span.fadeOut();
        }, 5000);
      }
    });
    </script>
</head>
<body>
  <div id="content">
    <label>Title</label>
    <p id = "title">
    </p>

    <label>Description</label>
    <p id="description">
    </p>

    <label>Author</label>
    <p id="author">
    </p>
  </div>
  <form action="./forms/logout.php" method="post">
    <input type="submit" value="Logout" />
  </form>
</body>
</html>
