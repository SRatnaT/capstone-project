
const WebSocket = require('ws')
const http = require('http')
const express = require('express')

// Creating a Express application 

const app = express()
app.use(express.json())


// Creating a HTTP server, linking it to express application 

const server = http.createServer(app)


// Create Websocket server

let wss

function createWSServer(port = 8080) {
    wss = new WebSocket.Server({ server })

    console.log(`WebSocket server running on ws://localhost:${port}`)

    wss.on('connection', (ws) => {
        console.log("New Client Connection");

        ws.on('message', (message) => {
            console.log(`Received: ${message}`);

            wss.clients.forEach(client => {
                if (client.readyState === WebSocket.OPEN) {
                    client.send(message.toString())
                }
            })
        })


    })

    return wss
}

// Creating an endpoint for Django to interact with Node

app.post('/broadcast', (req, res) => {

    console.log("BROADCAST HIT:", req.body);

    const payload = req.body

    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(payload.data))
        }
    })

    res.json({ status: "Message Broadcasted" })

})

// require.main === module only makes sure that the code within it is executed when the file is run from CLI

if (require.main === module) {
    createWSServer()

    // Starting the server

    server.listen(8080, () => {
        console.log('Node service running on http://localhost:8080');

    })
}




module.exports = { createWSServer }

