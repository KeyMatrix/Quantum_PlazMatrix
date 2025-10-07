const WebSocket = require('ws');
const { getAIAnswer } = require('./manage_json.js');

const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
  ws.on('message', (msg) => {
    const { query } = JSON.parse(msg);
    const answer = getAIAnswer(query);
    ws.send(JSON.stringify({ answer }));
  });
});
