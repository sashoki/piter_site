$(document).ready(function() {
    $("body").css("background", "#50B78A");
    $("footer, .top-bar, .top-bar ul").css("background", "#0E6B16");
    $(".callout").css("background", "#2BBB23");

    $(".thumb").attr("src", "/static/images/pythonfon.jpeg");


});

$(document).ready(function() {

    $("#menu").click(function(){ $("#list").slideToggle(1000)});

    $("#menu").mouseout(function(){ $("#menu").css("background-color", "#2BBB23")});
    $("#menu").mouseover(function(){ $("#menu").css("background-color", "#0E6B16")});


    $("#menu1").click(function(){ $("#list1").slideToggle(1000)});

    $("#menu1").mouseover(function(){ $("#menu1").css("background-color", "#0E6B16")});
    $("#menu1").mouseout(function(){ $("#menu1").css("background-color", "#2BBB23")});

});



