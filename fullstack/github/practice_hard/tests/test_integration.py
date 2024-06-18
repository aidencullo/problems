import unittest
import json
from app import app

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_user_task_integration(self):
        # Create a user
        new_user = {'username': 'testuser', 'email': 'test@example.com'}
        response = self.app.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        user_id = json.loads(response.data.decode('utf-8'))['id']

        # Create a task for the user
        new_task = {'title': 'New Task', 'description': 'Test Task Description', 'user_id': user_id}
        response = self.app.post('/tasks', json=new_task)
        self.assertEqual(response.status_code, 201)
        task_id = json.loads(response.data.decode('utf-8'))['id']

        # Retrieve all tasks for the user
        response = self.app.get(f'/users/{user_id}/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(task['id'] == task_id for task in json.loads(response.data.decode('utf-8'))))

if __name__ == '__main__':
    unittest.main()
