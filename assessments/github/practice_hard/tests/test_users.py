import unittest
import json
from app import app

class UsersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Initialize an empty list of users before each test
        self.users = []

    def tearDown(self):
        # Clean up by deleting all users after each test
        for user_id in self.users:
            self.app.delete(f'/users/{user_id}')

    def test_create_user(self):
        # Test creating a new user
        new_user = {'username': 'testuser', 'email': 'test@example.com'}
        response = self.app.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        created_user = json.loads(response.data.decode('utf-8'))
        self.assertEqual(created_user['username'], 'testuser')
        self.assertIn('id', created_user)  # Ensure the response contains an 'id'
        self.users.append(created_user['id'])  # Store the created user's id for cleanup

    def test_get_user_by_id(self):
        # Test retrieving a user by ID
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 404)  # Initially, no users should exist

        # Create a new user to test retrieval
        new_user = {'username': 'testuser', 'email': 'test@example.com'}
        response = self.app.post('/users', json=new_user)
        created_user = json.loads(response.data.decode('utf-8'))
        self.users.append(created_user['id'])  # Store the created user's id for cleanup

        # Now retrieve the user by ID
        response = self.app.get(f'/users/{created_user["id"]}')
        self.assertEqual(response.status_code, 200)
        retrieved_user = json.loads(response.data.decode('utf-8'))
        self.assertEqual(retrieved_user['username'], 'testuser')

    def test_update_user(self):
        # Test updating a user
        # Create a new user to update
        new_user = {'username': 'testuser', 'email': 'test@example.com'}
        response = self.app.post('/users', json=new_user)
        created_user = json.loads(response.data.decode('utf-8'))
        self.users.append(created_user['id'])  # Store the created user's id for cleanup

        # Update the user's username
        updated_user = {'username': 'updateduser'}
        response = self.app.put(f'/users/{created_user["id"]}', json=updated_user)
        self.assertEqual(response.status_code, 200)
        updated_user_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(updated_user_data['username'], 'updateduser')

    def test_delete_user(self):
        # Test deleting a user
        # Create a new user to delete
        new_user = {'username': 'testuser', 'email': 'test@example.com'}
        response = self.app.post('/users', json=new_user)
        created_user = json.loads(response.data.decode('utf-8'))
        self.users.append(created_user['id'])  # Store the created user's id for cleanup

        # Delete the user
        response = self.app.delete(f'/users/{created_user["id"]}')
        self.assertEqual(response.status_code, 204)

        # Ensure the user is deleted by trying to retrieve it again
        response = self.app.get(f'/users/{created_user["id"]}')
        self.assertEqual(response.status_code, 404)

    def test_get_all_users(self):
        # Test retrieving all users
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        users_list = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(users_list), len(self.users))  # Ensure all created users are retrieved

if __name__ == '__main__':
    unittest.main()

