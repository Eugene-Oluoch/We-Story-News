$('#hamburger').click(() => {
    $('#menu').slideToggle();
    setTimeout(() => {
        $('#menu').slideUp();
    }, 2000)
});