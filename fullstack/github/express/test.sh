curl -i http://localhost:3000/users
curl -i http://localhost:3000/users/1
curl -i -X POST -H "Content-Type: application/json" -d '{"name": "Alice"}' http://localhost:3000/users
curl -i http://localhost:3000/users
curl -i -X PUT -H "Content-Type: application/json" -d '{"id": "1", "name": "Updated Name"}' http://localhost:3000/users/1
curl -i -X DELETE http://localhost:3000/users/1
