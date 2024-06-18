import unittest
import json
from app import app

class TaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.tasks = []  # Initialize an empty list of tasks before each test

    def tearDown(self):
        # Clean up by deleting all tasks after each test
        for task_id in self.tasks:
            self.app.delete(f'/tasks/{task_id}')

    def test_create_task(self):
        # Test creating a new task
        new_task = {'title': 'Task 1', 'description': 'Description of Task 1', 'user_id': 1}
        response = self.app.post('/tasks', json=new_task)
        self.assertEqual(response.status_code, 201)
        created_task = json.loads(response.data.decode('utf-8'))
        self.assertEqual(created_task['title'], 'Task 1')
        self.assertIn('id', created_task)  # Ensure the response contains an 'id'
        self.tasks.append(created_task['id'])  # Store the created task's id for cleanup

    def test_get_task_by_id(self):
        # Test retrieving a task by ID
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 404)  # Initially, no tasks should exist

        # Create a new task to test retrieval
        new_task = {'title': 'Task 1', 'description': 'Description of Task 1', 'user_id': 1}
        response = self.app.post('/tasks', json=new_task)
        created_task = json.loads(response.data.decode('utf-8'))
        self.tasks.append(created_task['id'])  # Store the created task's id for cleanup

        # Now retrieve the task by ID
        response = self.app.get(f'/tasks/{created_task["id"]}')
        self.assertEqual(response.status_code, 200)
        retrieved_task = json.loads(response.data.decode('utf-8'))
        self.assertEqual(retrieved_task['title'], 'Task 1')

    def test_update_task(self):
        # Test updating a task
        # Create a new task to update
        new_task = {'title': 'Task 1', 'description': 'Description of Task 1', 'user_id': 1}
        response = self.app.post('/tasks', json=new_task)
        created_task = json.loads(response.data.decode('utf-8'))
        self.tasks.append(created_task['id'])  # Store the created task's id for cleanup

        # Update the task's title
        updated_task = {'title': 'Updated Task 1'}
        response = self.app.put(f'/tasks/{created_task["id"]}', json=updated_task)
        self.assertEqual(response.status_code, 200)
        updated_task_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(updated_task_data['title'], 'Updated Task 1')

    def test_delete_task(self):
        # Test deleting a task
        # Create a new task to delete
        new_task = {'title': 'Task 1', 'description': 'Description of Task 1', 'user_id': 1}
        response = self.app.post('/tasks', json=new_task)
        created_task = json.loads(response.data.decode('utf-8'))
        self.tasks.append(created_task['id'])  # Store the created task's id for cleanup

        # Delete the task
        response = self.app.delete(f'/tasks/{created_task["id"]}')
        self.assertEqual(response.status_code, 204)

        # Ensure the task is deleted by trying to retrieve it again
        response = self.app.get(f'/tasks/{created_task["id"]}')
        self.assertEqual(response.status_code, 404)

    def test_get_all_tasks(self):
        # Test retrieving all tasks
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        tasks_list = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(tasks_list), len(self.tasks))  # Ensure all created tasks are retrieved

if __name__ == '__main__':
    unittest.main()

