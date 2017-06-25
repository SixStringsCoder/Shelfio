/*
 Created on June 16th by Steve Hanlon.  JS file for collection app.
*/



/*---------------------------
 MODAL WINDOW - DETAIL VIEW
-----------------------------*/

// Show the Modal window
$('.myBtn').on('click', function() {
    let this_pic = $(this).attr("data-collectible");
    $('#galleryModal_' + this_pic).css('display', 'block');
});

// Hide the modal window
$('.close').on('click', function() {
    $('.modal').css('display','none');
});