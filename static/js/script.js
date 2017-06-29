/*
 Created on June 16th by Steve Hanlon.  JS file for collection app.
*/



/*---------------------------
 MODAL WINDOW - DETAIL VIEW
-----------------------------*/

// Show the Modal window
$('.myBtn').on('click', function() {
    let this_pic = $(this).attr("data-collectible");
    $('#galleryModal_' + this_pic).fadeIn('slow');
});

// Hide the modal window
$('.close').on('click', function() {
    $('.modal').fadeOut('fast');
});


/*----------------------------
         EMBED CODE
-----------------------------*/

// Show the Embed Code input text field
$('.embed_code_btn').click(function() {
    console.log('Embed code button clicked!');
   $('.embed_code_field').show('slow');
});