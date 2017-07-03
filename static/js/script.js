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


// Show EDIT-ADD-VIEW BUTTON AREA in Collectible, Modal and Embed
$('#edit_show').on('click', function() {
   $('#collectible_option_btns').slideDown('slow');
   $('#edit_show').fadeOut( 1 );
   $('#edit_hide').fadeIn( 1000 ).show('slow');
});

// Hides EDIT-ADD-VIEW BUTTON AREA in Collectible, Modal and Embed
$('#edit_hide').on('click', function(){
    $('#collectible_option_btns').slideUp('slow');
    $('#edit_hide').fadeOut( 1 );
    $('#edit_show').fadeIn( 1000 ).show('slow');
});

/*----------------------------
         EMBED CODE
-----------------------------*/

// Show the Embed Code input text field
$('.embed_code_btn').click(function() {
    console.log('Embed code button clicked!');
   $('.embed_code_field').show('slow');
});