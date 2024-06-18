# models.py
books = []

def get_all_books():
    return books

def get_book_by_id(book_id):
    return next((book for book in books if book['id'] == book_id), None)

def add_book(book):
    books.append(book)

def update_book(book_id, updated_book):
    book = get_book_by_id(book_id)
    if book:
        book.update(updated_book)
        return True
    return False

def delete_book(book_id):
    global books
    prev_len = len(books)
    books = [book for book in books if book['id'] != book_id]
    return len(books) != prev_len
