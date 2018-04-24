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

api.add_resource(login,'/')
api.add_resource(register,'/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)    