/*
 Created on June 16th by Steve Hanlon.  JS file for collection app.
*/

// FormSet Management

$('.link-formset').formset({
    addText: '&#x2b; Add Link',
    deleteText: '&#x2212 Remove'
});




// Change Form for New Collection form
(function($) {
    'use strict';
    $(document).ready(function() {
        var modelName = $('#django-admin-form-add-constants').data('modelName');
        $('body').on('click', '.add-another', function(e) {
            e.preventDefault();
            var event = $.Event('django:add-another-related');
            $(this).trigger(event);
            if (!event.isDefaultPrevented()) {
                showAddAnotherPopup(this);
            }
        });

        if (modelName) {
            $('form#' + modelName + '_form :input:visible:enabled:first').focus();
        }
    });
})(django.jQuery);


