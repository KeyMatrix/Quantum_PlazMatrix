const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (socket) => {
  console.log('Client connected');
  socket.send(JSON.stringify({ message: "Welcome!" }));

  socket.on('message', (data) => {
    const msg = JSON.parse(data);
    if (msg.query) {
      const answer = aiAnswer(msg.query);
      socket.send(JSON.stringify({ answer }));
    }
  });
});