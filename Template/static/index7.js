document.addEventListener('DOMContentLoaded', () => {
  // io.connect sets up a valid Connection to the websocket srored in a lsocket varaiable
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)
  // socket.on activates tyhe websocket to detect a particular function
  socket.on('connect', () => {
    // used this in debugging to show that the codes are working properly
    console.log("Connection established")
    document.querySelectorAll("button").forEach(function(button) {
      button.onclick = () => {
        // the datasetc value is accessed through the button.dataset.vote atrribute
        const selection = button.dataset.vote
        // used it for debugging
        console.log("Vote collected")
        // socket.emit sends a particular function to the srever called 'submit vote' storing my selection in a selection json object variable to access later in my flask app
        socket.emit('submit vote', {'selection': selection})
        console.log("Vote Emmited")
      }
    });

  })
  // detects the function 'announce vote'
  // defining a function called data
  socket.on('announce vote', data => {
    // all console.log are for debugging purpose
    console.log("Vote Announced")
    // create a new element li
    const li = document.createElement('li');
    li.innerHTML = `vote recorded: ${data.selection}`;
    document.querySelector('#votes').append(li);
    console.log("Vote displayed")
  })
})
