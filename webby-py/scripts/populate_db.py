import sys
sys.path.append('src')
from models.books import create_book

books = [
    {"Title": "Shadows of the Forgotten Realm", "Author": "Elena Marlowe", "ISBN": "978-1-4028-9462-1", "Year": 2018},
    {"Title": "The Quantum Cipher", "Author": "Drake Hollander", "ISBN": "978-0-553-29841-7", "Year": 2021},
    {"Title": "Gardens of Silent Winter", "Author": "Nora Winslow", "ISBN": "978-1-250-88721-9", "Year": 2015},
    {"Title": "City of Iron Stars", "Author": "Marcus Vey", "ISBN": "978-0-316-43228-0", "Year": 2022},
    {"Title": "A Study in Chiaroscuro", "Author": "Helen Sato", "ISBN": "978-1-847-22918-4", "Year": 2012},
    {"Title": "The Last Voyager", "Author": "Rafael Cortez", "ISBN": "978-1-9848-7231-6", "Year": 2019},
    {"Title": "Wildlands: A Naturalist's Journey", "Author": "Brianna Keene", "ISBN": "978-0-399-58211-3", "Year": 2016},
    {"Title": "Under the Painted Sky", "Author": "Colin Hartwood", "ISBN": "978-1-5247-2300-8", "Year": 2020},
    {"Title": "Algorithm of the Mind", "Author": "Dr. Lionel Chase", "ISBN": "978-1-7329-4210-1", "Year": 2023},
    {"Title": "The Secret of Briarwood Hall", "Author": "Adele Fairchild", "ISBN": "978-0-06-298321-7", "Year": 2014},
    {"Title": "Beyond the Western Ridge", "Author": "Trevor Bale", "ISBN": "978-1-56976-842-5", "Year": 2010},
    {"Title": "Moonlight Over Verona", "Author": "Gianna Belmonte", "ISBN": "978-0-7432-9895-4", "Year": 2017},
    {"Title": "Fragments of the Past", "Author": "Samuel Price", "ISBN": "978-1-7824-1198-0", "Year": 2011},
    {"Title": "Lingua of the Lost Isles", "Author": "Priya Raman", "ISBN": "978-1-5098-8833-2", "Year": 2024},
    {"Title": "The Ember King", "Author": "Gareth Lowell", "ISBN": "978-1-62087-661-0", "Year": 2013},
    {"Title": "Signal in the Dark", "Author": "Mason Rourke", "ISBN": "978-1-4028-9144-6", "Year": 2022},
    {"Title": "Café on Crescent Street", "Author": "Martine Dupré", "ISBN": "978-0-345-90231-2", "Year": 2016},
    {"Title": "Blueprints for Tomorrow", "Author": "Dr. Evelyn Ford", "ISBN": "978-1-64876-512-3", "Year": 2020},
    {"Title": "A Storm Beneath the Earth", "Author": "Haruto Nakamura", "ISBN": "978-4-88990-312-8", "Year": 2023},
    {"Title": "Echoes of the Painted Desert", "Author": "Sierra Callahan", "ISBN": "978-1-93325-889-0", "Year": 2018}
]

added_count = 0
failed_count = 0

print("Creating database and adding books...")
print()

for book in books:
    success = create_book(
        title=book["Title"],
        author=book["Author"], 
        isbn=book["ISBN"],
        year=book["Year"]
    )
    if success:
        added_count += 1
        print(f"✓ Added: {book['Title']} by {book['Author']}")
    else:
        failed_count += 1
        print(f"✗ Failed to add: {book['Title']} (ISBN may already exist)")

print()
print(f"Summary: {added_count} books added successfully, {failed_count} failed")