const books = require('./books.data.json');

const saveBooksToFile = () => {
	const fs = require('fs');
	fs.writeFileSync(
		'./src/models/books.data.json',
		JSON.stringify(books, null, 2)
	);
}

const getAllBooks = () => {
	return books;
}

const getBookByISBN = (isbn) => {
	return books.find(book => book.ISBN === isbn);
}

const addBook = ({ title, author, ISBN, year }) => {
	books.push({ "Title": title, "Author": author, "ISBN": ISBN, "Year": Number(year) });

	saveBooksToFile();

	return { "Title": title, "Author": author, "ISBN": ISBN, "Year": Number(year) };
}

const updateBook = ({ ISBN, title, author, year }) => {
	const bookIndex = books.findIndex(book => book.ISBN === ISBN);
	if (bookIndex !== -1) {
		const oldBook = books[bookIndex];
		const newBook = {
			"Title": title || oldBook.Title,
			"Author": author || oldBook.Author,
			"ISBN": ISBN,
			"Year": year ? Number(year) : oldBook.Year
		}
		books[bookIndex] = newBook;
		saveBooksToFile();
		return books[bookIndex];
	}
	return null;
}

const deleteBook = (isbn) => {
	const bookIndex = books.findIndex(book => book.ISBN === isbn);
	if (bookIndex !== -1) {
		const deletedBook = books.splice(bookIndex, 1);
		saveBooksToFile();
		return deletedBook[0];
	}
	return null;
}

module.exports = {
	getAllBooks,
	getBookByISBN,
	addBook,
	updateBook,
	deleteBook
};
