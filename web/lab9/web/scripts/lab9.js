const getPuzzleUrl = '/puzzle';

$(document).ready(function(){
    var prevId = null;
    console.log("ready document");
    $('.puzzlepiece').click(function() {
        console.log("clicked " + $(this).attr("id"));
        var id = $(this).attr("id");
        if(prevId == null) {
            prevId = id;
            $("#msg").text("Now click another one to make a swap!");
            $("#selected").attr("src", "img/" + id + ".jpeg");
            return ;
        }
        else {
            console.log("swap ( " + id + ", " + prevId + " )");
            $.ajax({
                url: getPuzzleUrl,
                type: "PUT",
                data: {
                    "id1": id,
                    "id2": prevId
                },
                success: function(res) {
                    console.log("success: " + res);
                    window.location = window.location.pathname;
                }
            });
            $("#selected").removeAttr("src");
            prevId = null;
        }
    });
    $("#selected").click(function() {
        prevId = null;
        $(this).removeAttr("src");
        $("#msg").text("Click on an image to make a swap!");
    });
});
