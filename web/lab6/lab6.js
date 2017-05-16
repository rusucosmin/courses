var img_arr = []

function shuffle(a) {
  var j, x, i;
  for (i = a.length; i; i--) {
    j = Math.floor(Math.random() * i);
    x = a[i - 1];
    a[i - 1] = a[j];
    a[j] = x;
  }
}

function init() {
  for(x = 0; x < 3; ++ x)
    for(y = 0; y < 3; ++ y) {
      img = new Image();
      img.src = "img/" + x + '-' + y + ".jpeg";
      img.className = "puzzlepiece";
      img.id = x * 3 + y;
      img.width = 100;
      img.height = 100;
      img.onclick = function() {
        imgClick(this);
      }
      img_arr.push(img);
    }
  shuffle(img_arr);
  showPuzzle();
}

function showPuzzle() {
  var puzzle = "";
  document.getElementById('puzzle').innerHTML = "";
  var done = true;
  for(var x = 0; x < img_arr.length; ++ x) {
    if(img_arr[x].id != x)
      done = false;
    document.getElementById('puzzle').appendChild(img_arr[x]);
    console.log(img_arr[x]);
  }
  if(done)
    document.getElementById("status").innerHTML = "<p>CONGRATS!</p>";
}

var toSwap = null;
var indexToSwap = null;
function imgClick(img) {
  if(toSwap == null) {
    toSwap = img;
    indexToSwap = img_arr.indexOf(img);
    document.getElementById('status').innerHTML = "<p>Chosen image (click on it to cancel swap):</p>";
    var copy = new Image();
    copy.src = img.src;
    copy.width = img.width;
    copy.height = img.height;
    copy.className = img.className;
    copy.onclick = function() {
      document.getElementById('status').innerHTML = "";
      toSwap = null;
      indexToSwap = null;
    }
    document.getElementById('status').appendChild(copy);
    return ;
  }
  document.getElementById('status').innerHTML = "";
  index = img_arr.indexOf(img);
  img_arr[indexToSwap] = img;
  img_arr[index] = toSwap;
  showPuzzle();
  toSwap = null;
  indexToSwap = null;
}
