
$(document).ready(function() {
    console.log($("#carousel-slides").children()[0]);
    console.log(5);
    $("#carousel-slides").children()[0].className = "item active";
});

// Closes the sidebar menu
$("#menu-close").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
});

// Opens the sidebar menu
$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
});

$('.carousel').carousel({
    interval: 5000 //changes the speed
})



