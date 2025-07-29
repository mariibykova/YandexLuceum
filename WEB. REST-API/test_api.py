import unittest
import requests

BASE_URL = 'http://127.0.0.1:5000/api/v2'

class TestAPI(unittest.TestCase):
    def test_get_all_users(self):
        response = requests.get(f'{BASE_URL}/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_user_by_id(self):
        response = requests.get(f'{BASE_URL}/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('username', response.json())

    def test_create_user(self):
        user_data = {'username': 'testuser', 'email': 'test@example.com'}
        response = requests.post(f'{BASE_URL}/users', json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['username'], 'testuser')

    def test_delete_user(self):
        response = requests.delete(f'{BASE_URL}/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'User deleted.')

    def test_get_all_jobs(self):
        response = requests.get(f'{BASE_URL}/jobs')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_job_by_id(self):
        response = requests.get(f'{BASE_URL}/jobs/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.json())

    def test_create_job(self):
        job_data = {'title': 'Developer', 'description': 'Develop stuff', 'user_id': 1}
        response = requests.post(f'{BASE_URL}/jobs', json=job_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], 'Developer')

    def test_delete_job(self):
        response = requests.delete(f'{BASE_URL}/jobs/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Job deleted.')

if __name__ == '__main__':
    unittest.main()
