
const WebSocket = require('ws')
const http = require('http')
const express = require('express')

// Creating a Express application 

const app = express()
app.use(express.json())


// Creating a HTTP server, linking it to express application 

const server = http.createServer(app)

// Heavy and Slow Function 

function factorial(n) {


    if (n == 0 || n == 1) return 1

    return n * factorial(n - 1)

}

function fakeDBCall() {

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Suceess")
        }, 2000)
    })
}



// Create Websocket server

let wss

function createWSServer(port = 8080) {
    wss = new WebSocket.Server({ server })

    console.log(`WebSocket server running on ws://localhost:${port}`)

    wss.on('connection', (ws) => {
        console.log("New Client Connection");

        // ws.on('message', (message) => {
        //     console.log(`Received: ${message}`);

        //     wss.clients.forEach(client => {
        //         if (ws !== client && client.readyState === WebSocket.OPEN) {
        //             client.send(message.toString())
        //         }
        //     })
        // })

        // BUGGED VERSION FOR DEBUGGING PURPOSE

        ws.on('message', (message) => {
            console.log(`Received: ${message}`);

            // BUG: typo in readyState check
            wss.clients.forEach(client => {
                if (ws !== client && client.readyState === WebSocket.OPEN) {
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

    // wss.clients.forEach((client) => {
    //     if (client.readyState === WebSocket.OPEN) {
    //         client.send(JSON.stringify(payload.data))
    //     }
    // })

    //BUGGED CODE:
    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(payload.data))
        }
    })

    res.json({ status: "Message Broadcasted" })

})

app.get("/fake-node-get", async (req, res) => {

    try {

        const data = await fakeDBCall()

        res.json({ data: data })


    } catch (err) {

        console.error(err)

    }

})

app.get("/slow-api", (req, res) => {
    const data = factorial(100)

    res.json({ data: data })
})

// require.main === module only makes sure that the code within it is executed when the file is run from CLI

if (require.main === module) {
    // Starting the server

    server.listen(8080, () => {
        console.log('Node service running on http://localhost:8080');

    })
    createWSServer()


}





module.exports = { createWSServer }

