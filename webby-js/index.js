const express = require('express')
const app = express()
const port = 3000

app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(express.static('public'))

app.get('/web', (req, res) => {
  res.send('Hello from Web!')
})

app.get('/api', (req, res) => {
  res.json({ message: 'Hello from API!' })
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
