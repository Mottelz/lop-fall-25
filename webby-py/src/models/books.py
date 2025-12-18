import sqlite3
import os
from typing import List, Optional, Dict, Any


def _init_database(db_path: str = "books.db"):
    with sqlite3.connect(db_path) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                isbn TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        ''')
        conn.commit()


def create_book(title: str, author: str, isbn: str, year: int, db_path: str = "books.db") -> bool:
    _init_database(db_path)
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(
                'INSERT INTO books (title, author, isbn, year) VALUES (?, ?, ?, ?)',
                (title, author, isbn, year)
            )
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        # ISBN already exists
        return False


def get_book_by_isbn(isbn: str, db_path: str = "books.db") -> Optional[Dict[str, Any]]:
    _init_database(db_path)
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute('SELECT * FROM books WHERE isbn = ?', (isbn,))
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None


def get_all_books(db_path: str = "books.db") -> List[Dict[str, Any]]:
    _init_database(db_path)
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute('SELECT * FROM books ORDER BY title')
        rows = cursor.fetchall()
        return [dict(row) for row in rows]


def update_book(isbn: str, title: str = None, author: str = None, year: int = None, db_path: str = "books.db") -> bool:
    _init_database(db_path)
    
    # First check if the book exists
    if not get_book_by_isbn(isbn, db_path):
        return False
    
    # Build the update query dynamically based on provided fields
    update_fields = []
    update_values = []
    
    if title is not None:
        update_fields.append('title = ?')
        update_values.append(title)
    
    if author is not None:
        update_fields.append('author = ?')
        update_values.append(author)
    
    if year is not None:
        update_fields.append('year = ?')
        update_values.append(year)
    
    if not update_fields:
        # No fields to update
        return True
    
    update_values.append(isbn)  # Add ISBN for WHERE clause
    
    query = f'UPDATE books SET {", ".join(update_fields)} WHERE isbn = ?'
    
    with sqlite3.connect(db_path) as conn:
        conn.execute(query, update_values)
        conn.commit()
        return True


def delete_book(isbn: str, db_path: str = "books.db") -> bool:
    _init_database(db_path)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute('DELETE FROM books WHERE isbn = ?', (isbn,))
        conn.commit()
        return cursor.rowcount > 0


def search_books(title: str = None, author: str = None, year: int = None, db_path: str = "books.db") -> List[Dict[str, Any]]:
    _init_database(db_path)
    conditions = []
    values = []
    
    if title:
        conditions.append('title LIKE ?')
        values.append(f'%{title}%')
    
    if author:
        conditions.append('author LIKE ?')
        values.append(f'%{author}%')
    
    if year:
        conditions.append('year = ?')
        values.append(year)
    
    if not conditions:
        return get_all_books(db_path)
    
    query = f'SELECT * FROM books WHERE {" AND ".join(conditions)} ORDER BY title'
    
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(query, values)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]


def count_books(db_path: str = "books.db") -> int:
    _init_database(db_path)
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute('SELECT COUNT(*) FROM books')
        return cursor.fetchone()[0]


# Alias functions for convenience (keeping the same names)
def get_book(isbn: str, db_path: str = "books.db") -> Optional[Dict[str, Any]]:
    return get_book_by_isbn(isbn, db_path)
