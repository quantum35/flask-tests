from app import app
import unittest
import json


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"username":"quantum", "email":"quantum@gmail.com","password":"password"}


    def test_login(self):
        response = self.app.get('/')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Successfully Logged in")
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.post('/register', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["username"], "quantum")
        self.assertEqual(result["email"], "quantum@gmail.com")
        self.assertEqual(result["password"], "password")
        self.assertEqual(response.status_code, 201)



if __name__ == '__main__':
    unittest.main()
