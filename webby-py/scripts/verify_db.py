import sys
sys.path.append('src')
from models.books import get_all_books, count_books

print(f"Total books in database: {count_books()}")
print("\nAll books in database:")
print("-" * 50)

books = get_all_books()
for book in books:
    print(f"• {book['title']} by {book['author']} ({book['year']})")
    print(f"  ISBN: {book['isbn']}")
    print()