document.addEventListener('DOMContentLoaded', () => {
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port)
  socket.on('connect', () => {
    console.log("Connection established")
    document.querySelectorAll("button").forEach(function(button) {
      button.onclick = () => {
        const selection = button.dataset.vote
        console.log("Vote collected")
        socket.emit('submit vote', {'selection': selection})
        console.log("Vote Emmited")
      }
    });

  })
  socket.on('vote totals', data => {
    console.log("Vote Announced")
    document.querySelector('#yes').innerHTML = data.yes;
      document.querySelector('#no').innerHTML = data.no;
        document.querySelector('#maybe').innerHTML = data.maybe;
    console.log("Vote displayed")
  })
})
