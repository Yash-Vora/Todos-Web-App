// JQuery For Validation

// Initialize JQuery
$(document).ready(function(){
    // Title Validation
    $('#Title').blur(function(){
        $('#TitleValidation').empty();
        if($(this).val() == '') {
            $('#TitleValidation').html('Field is mandatory...!');
        } 
    });

    // Feedback Validation
    $('#Description').blur(function(){
        $('#DescriptionValidation').empty();
        if($(this).val() == '') {
            $('#DescriptionValidation').html('Field is mandatory...!');
        }  
    });
});