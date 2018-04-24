from flask import Flask, request, make_response
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)


class login(Resource):
    def get(self):
        return {'message':'Successfully Logged in'},200


class register(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        return {'username':'quantum',
                'email':'quantum@gmail.com',
                'password':'password'
                },201
#Admin
class addNewMeal(Resource):
    def post(self):
        data = request.get_json()
        meal_id = data['meal_id']
        name = data['name']
        price = data['price']
        return {'meal_id':'meal1',
                'name':'Chips',
                'price':'1000'
                },201
class modifyMeal(Resource):
    def put(self):
        data = request.get_json()
        meal_id = data['meal_id']
        name = data['name']
        price = data['price']
        return {
                'meal_id':'1',
                'name':'Ugali',
                'price':'500'
                },201
class deleteMealOption(Resource):
    def delete(self):
        data = request.get_json()
        meal_id = data['meal_id']
        name = data['name']
        price = data['price']
        return {'meal_id':'meal1',
                'name':'Chips',
                'price':'1000'
                },201
        

class setUpmealDay(Resource):
     def post(self):
        data = request.get_json()
        meal_id = data['id']
        name = data['mname']
        price = data['mprice']
        return {'meal_id':'meal1',
                'name':'Chips',
                'price':'1000'
                },201
class checkOrdersMadebyUser(Resource):
    def get(self):
        return {'message':'Here are The Orders Made by users'}

class checkTodaysProfit(Resource):
    def get(self):
        return {'message':'Todays Profit is'}
class checkOrderHistoryAdmm(Resource):
    def get(self):
        return {'message':'Here is Your History'}
class checkLogedinAdmins(Resource):
    def get(self):
        return {'message':'Return More Than one Admin Loged In'}
#Customers
class custCheckMenu(Resource):
    def get(self):
        return{'message':'Here is your Menu Of the Day'}
    def post(self):
        data = request.get_json()
        name = data['name']
        price = data['price']
        return {'name':'ugali',
                'price':'1000'
                },201
class checkOrderHistory(Resource):
    def get(self):
        return{'message':'Here is your Order History'}

class getNotification(Resource):
    def get(self):
        return{'message':'You have one New Message'}


api.add_resource(login,'/')
api.add_resource(register,'/register')
api.add_resource(deleteMealOption,'/detemeal')
api.add_resource(addNewMeal, '/addNewMeal')
api.add_resource(modifyMeal,'/modifyMeal')
api.add_resource(custCheckMenu,'/custCheckMenu')
api.add_resource(checkOrdersMadebyUser,'/checkOrdersMadebyUser')
api.add_resource(checkTodaysProfit,'/checkTodaysProfit')
api.add_resource(checkOrderHistory,'/checkOrderHistory')
api.add_resource(getNotification,'/getNotification')
api.add_resource(checkOrderHistoryAdmm,'/checkOrderHistoryAdmm')
api.add_resource(checkLogedinAdmins,'/checkLogedinAdmins')
if __name__ == '__main__':
    app.run(port=5000, debug=True)    