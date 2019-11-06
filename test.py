import unittest
from app import app


class MongoFlaskProjectTest(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

# Running the tests
if __name__ == '__main__':
    unittest.main()