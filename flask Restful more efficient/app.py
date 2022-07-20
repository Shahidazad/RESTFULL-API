from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity # json web token private mssge in encode bwt user & api

from security import authenticate, identity

app = Flask(__name__)  #create app
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


# class Student(Resource):   # student is resource
#     def get(self,name):
#         return {'student':name}  # http://127.0.0.12:5000/student/jhon (how to access)

# api.add_resource(Student,'/student/<string>:name')  

class Item(Resource):   # item is resource
    parser = reqparse.RequestParser()  # only price should pass no other this should pass funtn of requestparse 
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        return {'item': next(filter(lambda x: x['name'] == name, items), None)}# give first item 
    # get check in items list if name matches or not 
    def post(self, name):   # create new item add to database
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}
        # 400 is bad request by user
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item

    # @jwt_required()
    def delete(self, name): 
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    # @jwt_required()
    def put(self, name):  #  create or update items
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:  # if item is not found then create item   
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item # no need of jsonnify restful automatically do that

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True(show error message)