var Billboard = {}

Billboard.init = function () {
    $(document).ready(function () {
        Billboard.bindAddButton();
    });
};
Billboard.bindAddButton = function() {
    //initialize transaction
    $('#add_post_btn').on('click', function () {
        $('#add_post_form').fadeIn();
        $('#close_post_btn').show();
        $('#check_post_btn').show();
        $('#add_post_btn').hide();
    });
    //cancel transaction
    $('#close_post_btn').on('click', function () {
        $('#add_post_form').fadeOut();
        $('#close_post_btn').hide();
        $('#check_post_btn').hide();
        $('#add_post_btn').fadeIn();
    });
    //send post request
    $('#check_post_btn').on('click', function() {
        $('#add_post_form').submit();
    });
    //submitting add post form
    $('#add_post_form').on('submit', function(e) {
        console.log($('#add_post_form').serialize());
    });
}

Billboard.init();