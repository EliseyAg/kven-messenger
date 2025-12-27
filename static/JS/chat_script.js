var socket = io.connect(
    window.location.protocol + "//" + document.domain + ":" + location.port
);

socket.on("connect", function () {
  console.log("Connected...!", socket.connected);
});


function post_message()
{
    const usernameInput = document.querySelector('input[name="message"]');
    socket.emit("message_sent");Sma
}

const form = document.getElementById('post_message_form');
form.addEventListener('submit', post_message());
