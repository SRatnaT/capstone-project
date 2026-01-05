
const WebSocket = require('ws')
const { createWSServer } = require('../server')

let wss

const PORT = 8090
const URL = `ws://localhost:${PORT}`

beforeAll(() => {
    wss = createWSServer(PORT)
})

afterAll((done) => {
    wss.close(done)
})

// TEST 1: Checking That Server accepts connections

test("Client Can Connect to the WebSocket server", (done) => {

    const client = new WebSocket(URL)

    client.on('open', () => {
        expect(client.readyState).toBe(WebSocket.OPEN)
        client.close()
        done()
    })

})

// TEST 2: Checking that the message is broadcasted to all the clients of the websocket

test("Message is broadcasted to all the connected clients", (done) => {


    let broadcastedCount = 0

    const client1 = new WebSocket(URL)
    const client2 = new WebSocket(URL)

    function messageSent() {

        broadcastedCount++

        if (broadcastedCount == 2) {
            console.log("All the clients received the message");

            client1.close()
            client2.close()
            done()
        }

    }

    client1.on("open", () => {
        client2.on("open", () => {
            client1.send("Hello World")
        })
    })

    client1.on('message', (msg) => {
        expect(msg.toString()).toBe('Hello World')
        messageSent()
    })

    client2.on('message', (msg) => {
        expect(msg.toString()).toBe('Hello World')
        messageSent()
    })



})

// TEST 3: Disconnected User does not receive any broadcasted message

test("Disconnected Client does not receive any message", (done) => {

    const client1 = new WebSocket(URL)
    const client2 = new WebSocket(URL)

    client2.on('open', () => {
        client2.close()
        console.log("Client 2 Disconnected");
        
    })

    client1.on('open', () => {
        setTimeout(() => {
            client1.send("Client 1 Test Message")
        }, 100)
    })

    client1.on('message', (msg) => {
        console.log("CLIENT 1 RECEIVED");
        expect(msg.toString()).toBe("Client 1 Test Message")

    })

    client2.on("message", (msg) => {
        // Should not be called
        throw new Error('Disconnected Client Received Broadcasted message')
    })

    setTimeout(() => {
        client1.close()
        done()
    }, 300)

})
