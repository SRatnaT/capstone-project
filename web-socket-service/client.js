
const WebSocket = require('ws')

const ws = new WebSocket("ws://localhost:8080")

// Connection Open

ws.on('open', () => {
    console.log("Connected to the server");

    // Send a message

    ws.send('Hello From Node Client 3')
    
})

ws.on('message' , (message) => {
    console.log(`Received from server: ${message}`);
    
})

ws.on('close', () => {
    console.log('Disconnected from server');
});