curl -X GET -i http://127.0.0.1:5000/books
curl -X POST -i http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"id": 1, "title": "1984", "author": "George Orwell", "published_date": "1949-06-08"}'
curl -X GET -i http://127.0.0.1:5000/books/1
curl -X PUT -i http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"title": "1984", "author": "George Orwell", "published_date": "1950-06-08"}'
curl -X DELETE -i http://127.0.0.1:5000/books/1
