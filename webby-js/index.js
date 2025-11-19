const express = require('express')
const app = express()
const port = 3000

const booksModel = require('./src/models/books.js')

app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(express.static('public'))

app.get('/', (req, res) => {
  res.json({ message: 'I\'m ALIVE!!!' })
})

app.get('/books', (req, res) => {
  const books = booksModel.getAllBooks();
  res.json(books);
})

app.post('/books', (req, res) => {
  const { title, author, ISBN, year } = req.body;
  const newBook = booksModel.addBook({ title, author, ISBN, year });
  res.status(201).json(newBook);
})

app.get('/books/:isbn', (req, res) => {
  const isbn = req.params.isbn;
  const book = booksModel.getBookByISBN(isbn);
  if (book) {
    res.json(book);
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
})

app.patch('/books/:isbn', (req, res) => {
  const isbn = req.params.isbn;
  const { title, author, year } = req.body;
  const updatedBook = booksModel.updateBook({ ISBN: isbn, title, author, year });
  if (updatedBook) {
    res.json(updatedBook);
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
})

app.delete('/books/:isbn', (req, res) => {
  const isbn = req.params.isbn;
  const deletedBook = booksModel.deleteBook(isbn);
  if (deletedBook) {
    res.json(deletedBook);
  } else {
    res.status(404).json({ message: 'Book not found' });
  }
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
