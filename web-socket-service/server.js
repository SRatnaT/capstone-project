
const WebSocket = require('ws')

// Create Websocket server

const wss = new WebSocket.Server({port: 8080})

console.log("WebSocket server running on ws://localhost:8080")

// New Client Connection Handling

wss.on('connection' , (ws) => {
    console.log("New client connection:");

    // When Client sends Message

    ws.on('message' , (message) => {
        console.log(`Received: ${message}`);

        // Broadcast the message to all the clients

        wss.clients.forEach((client) => {

            if(client.readyState === WebSocket.OPEN){
                client.send(message.toString())
            }
        })
        
    })

    // Connection Close Handling

    ws.on('close' , () => {
        console.log("Client disconnected from WS server")
    })
    
})