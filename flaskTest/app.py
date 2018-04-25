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
class UpdatemealOption(Resource):
    def put(self,mealid):
        data11 = request.get_json()
        meal_id = data11['meal_id']
        name = data11['name']
        price = data11['price']
        return {
                'meal_id':'meal1',
                'name':'Ugali',
                'price':'500'
                },201
class modifyMeal(Resource):
    def put(self,menuid):
        meal_id = 'meal1'
        name = 'Ugali'
        price = '500'
        return {
                'meal_id':'meal1',
                'name':'Ugali',
                'price':'500'
                },201
class deleteMealOption(Resource):
    def delete(self,mealid):
        data1 = request.get_json()
        meal_id = data1['meal_id']
        name = data1['name']
        price = data1['price']
        return { 'message':'Meal Successfuly Deleted'
                },200
        

class setUpmealDay(Resource):
     def post(self):
        data1 = request.get_json()
        meal_id = data1['meal_id']
        name = data1['name']
        price = data1['price']
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


api.add_resource(login,'/auth/login')
api.add_resource(register,'/auth/register')
api.add_resource(addNewMeal, '/meals/')
api.add_resource(deleteMealOption,'/meals/<mealid>')
api.add_resource(UpdatemealOption,'/meals/<mealid>')
api.add_resource(setUpmealDay,'/menu/')
api.add_resource(modifyMeal,'/menu/<menuid>')
api.add_resource(custCheckMenu,'/users/menu/')
api.add_resource(checkOrdersMadebyUser,'/orders/')
api.add_resource(checkTodaysProfit,'/admin/profit')
api.add_resource(checkOrderHistory,'/users/orders')
api.add_resource(getNotification,'/users/notification')
api.add_resource(checkOrderHistoryAdmm,'/admin/orders')
api.add_resource(checkLogedinAdmins,'/admin/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)    