from app import app
import unittest
import json


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"username":"quantum", "email":"quantum@gmail.com","password":"password"}
        self.data1 = {"meal_id":"meal1", "name":"Chips","price":"1000"}
        self.data11 = {"meal_id":"meal1", "name":"Ugali","price":"500"}
        self.data2 = {"meal_id":"meal1", "name":"Ugali","price":"500"}
        self.data3 = {"meal_id":"meal1", "name":"Chips","price":"1000"}
        self.data4 = {"name":"ugali", "price":"1000"}

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
    
    def test_addNewMeal(self):
        response = self.app.post('/addNewMeal', data = json.dumps(self.data2) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], "meal1")
        self.assertEqual(result["name"], "Chips")
        self.assertEqual(result["price"], "1000")
        self.assertEqual(response.status_code, 201)

    def test_modifyMeal(self):
        response = self.app.put('/UpdatemealOption', data = json.dumps(self.data11) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], "meal1")
        self.assertEqual(result["name"], "Ugali")
        self.assertEqual(result["price"], "500")
        self.assertEqual(response.status_code, 201)

    def test_deleteMealOption(self):
        response = self.app.delete('/detemeal',data=json.dumps(self.data1),content_type = 'application/json' )
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Meal Successfuly Deleted")
        self.assertEqual(response.status_code, 200)

    def test_MealOfTheDay(self):
        response = self.app.post('/setUpmealDay', data = json.dumps(self.data1) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["meal_id"], "meal1")
        self.assertEqual(result["name"], "Chips")
        self.assertEqual(result["price"], "1000")
        self.assertEqual(response.status_code, 201)
    
    def test_OrdersMadeByUsers(self):
        response = self.app.get('/checkOrdersMadebyUser')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Here are The Orders Made by users")
        self.assertEqual(response.status_code, 200)
    def test_profitMade(self):
        response = self.app.get('/checkTodaysProfit')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Todays Profit is")
        self.assertEqual(response.status_code, 200)
    def test_admCheckOrderHistory(self):
        response = self.app.get('/checkOrderHistoryAdmm')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Here is Your History")
        self.assertEqual(response.status_code, 200)
    def test_noAdmin(self):
        response = self.app.get('/checkLogedinAdmins')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Return More Than one Admin Loged In")
        self.assertEqual(response.status_code, 200)

#Cutomers
    def test_custCheckDaysMenu(self):
        response = self.app.get('/custCheckMenu')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Here is your Menu Of the Day")
        self.assertEqual(response.status_code, 200)
    def test_changeMealChoice(self):
        response = self.app.put('/modifyMeal', data = json.dumps(self.data4) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["name"], "ugali")
        self.assertEqual(result["price"], "1000")
        self.assertEqual(response.status_code, 201)
    def test_checkOrderHistory(self):
        response = self.app.get('/checkOrderHistory')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Here is your Order History")
        self.assertEqual(response.status_code, 200)
    def test_getNotification(self):
        response = self.app.get('/getNotification')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "You have one New Message")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
