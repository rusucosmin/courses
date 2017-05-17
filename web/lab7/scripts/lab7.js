$(document).ready(function() {
  var intId;
  var score = 0;

  function addImage() {
    var ind = Math.floor(Math.random() * 9);
    var src = "img/" + ind + ".jpeg";
    var img = new Image();

    $(img).attr('src', src);
    $(img).css('position', 'absolute');
    $(img).css('margins', 'auto');
    $(img).css('left',$('#game').offset().left + Math.random() * 400);
    $(img).css('top',$('#game').offset().top + Math.random() * 400);
    $(img).css('height', 100);
    $(img).css('width', 100);
    $(img).click(function(){
      ++ score;
      if(score >= 10) {
        $("#message").text("You won. Score: " + score);
        clearInterval(intId);
      }
      else
        $("#message").text("Score: " + score);
    });
    $(img).fadeOut(2000);

    $("#game").append(img);
  }

  intId = window.setInterval(function() {
    addImage();
  }, 1000);
});
