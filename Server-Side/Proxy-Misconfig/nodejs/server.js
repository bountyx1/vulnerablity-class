const express = require('express')
const app = express()
const port = 3000

app.get('/debug', (req, res) => {
  res.send('flag nodejs')
})


app.get('/', (req, res) => {
  res.send('access node')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
