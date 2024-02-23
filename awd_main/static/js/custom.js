// Set a timer to execute a function after 4000 milliseconds (4 seconds)
setTimeout(function() {
    // Select the element with the ID "message" using jQuery
    $('#messages')
        // Apply the fadeOut effect with a 'slow' animation speed
        .fadeOut('slow');
}, 4000);