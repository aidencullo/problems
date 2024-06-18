const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

let users = [];

function generateUserId() {
    const maxId = users.reduce((max, user) => (user.id > max ? user.id : max), 0);
    return maxId + 1;
}

app.get('/users', (req, res) => {
  res.json(users);
});

app.get('/users/:id', (req, res) => {
  for (user of users) {
    if (user.id === req.params.id) {
      res.json(user);
      return;
    }
  }
  res.status(404).send('User not found');
});

app.post('/users', (req, res) => {
  const user = req.body;
  user.id = generateUserId();
  users.push(user);
  res.status(201).json(user);
});

app.put('/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  for (user of users) {
    if (user.id === id) {
      user = req.body;
      res.status(204).send();
      return;
    }
  }
  res.status(404).send('User not found');
});

app.delete('/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  numUsers = users.length;
  users = users.filter(user => user.id !== id);
  if (users.length < numUsers) {
		res.status(204).send();
	} else {
		res.status(404).send('User not found');
	}
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
