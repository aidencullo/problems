import unittest
import json
from app import app

class TasksTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json.loads(response.data.decode('utf-8')), list))

    def test_get_task_by_id(self):
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['id'], 1)

    def test_create_task(self):
        new_task = {'title': 'New Task', 'description': 'Test Task Description', 'user_id': 1}
        response = self.app.post('/tasks', json=new_task)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['title'], 'New Task')

    def test_update_task(self):
        updated_task = {'title': 'Updated Task'}
        response = self.app.put('/tasks/1', json=updated_task)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data.decode('utf-8'))['title'], 'Updated Task')

    def test_delete_task(self):
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
