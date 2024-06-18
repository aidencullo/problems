from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(message='Book added successfully'), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def replace_book(book_id):
    for book in books:
        if book['id'] == book_id:
            updated_book = request.json
            book.update(updated_book)
            return jsonify(message='Book updated successfully'), 200
    return jsonify(message='Book not found'), 404

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify(message='Book not found'), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def destroy_book(book_id):
    global books

    initial_length = len(books)
    books = [book for book in books if book['id'] != book_id]

    if len(books) < initial_length:
        return jsonify(message='Book deleted successfully'), 200
    else:
        return jsonify(message='Book not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
