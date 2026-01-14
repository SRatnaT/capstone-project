
const express = require('express')
const app = express()


app.get('/test-api', (req, res) => {
    res.send("Test Data Sent")
})

app.listen(3000, () => {
    console.log("The Test server is running on Port 3000");

})