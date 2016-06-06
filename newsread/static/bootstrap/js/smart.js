/**
 * Created by orelz on 05/06/2016.
 */
$(document).ready(function(){
    $(".hoverDiv").hover(function(){
        $(this).css("background", "#f5f5f5");
    }, function(){
        $(this).css("background", "#fff");
    });
    $(".navbar-custom").hover(function(){
        $(this).css("background", "#f5f5f5");
    }, function() {
        $(this).css("background", "#fff");
    });
});