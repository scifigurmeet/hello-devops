import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(response.data.decode(), 'Hello, DevOps!')

if __name__ == '__main__':
    unittest.main()