from flask import Flask, request
from markupsafe import escape
from src.models.books import get_all_books, get_book_by_isbn, create_book, update_book, delete_book

app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "IM ALIVE!!!"}

@app.route("/books")
def getAllBooks():
    return get_all_books()

@app.route("/books", methods=["POST"])
def addBook():
    book_data = request.json
    book_title = get_from_json("title", book_data)
    book_author = get_from_json("author", book_data)
    book_isbn = get_from_json("isbn", book_data)
    book_year = get_from_json("year", book_data)
    addedBook = create_book(isbn=book_isbn, title=book_title, author=book_author, year=book_year)
    if addedBook:
        return {"message": f"Book '{escape(book_title)}' added successfully!"}, 201
    else:
        return {"message": f"Book with ISBN '{escape(book_isbn)}' already exists."}, 409

@app.route("/books/<string:isbn>")
def getBookByISBN(isbn):
	book = get_book_by_isbn(isbn)
	if not book:
		return {"message": f"Book with ISBN '{escape(isbn)}' not found."}, 404
	return {"book": book}, 200

@app.route("/books/<string:isbn>", methods=["PATCH"])
def updateBookByISBN(isbn):
    book_data = request.json
    book_title = get_from_json("title", book_data)
    book_author = get_from_json("author", book_data)
    book_year = get_from_json("year", book_data)
    updated = update_book(isbn=isbn, title=book_title, author=book_author, year=book_year)
    if updated:
        return {"message": f"Book with ISBN '{escape(isbn)}' updated successfully!"}, 200
    else:
        return {"message": f"Book with ISBN '{escape(isbn)}' not found."}, 404

@app.route("/books/<string:isbn>", methods=["DELETE"])
def deleteBookByISBN(isbn):
	deleted_count = delete_book(isbn)
	if deleted_count == 0:
		return {"message": f"Book with ISBN '{escape(isbn)}' not found."}, 404
	else:
		return {"message": f"Book with ISBN '{escape(isbn)}' deleted successfully!"}, 200


def get_from_json(key, data, default=None):
    for field in data:
        if field["name"] == key:
            return field["value"]
    return default