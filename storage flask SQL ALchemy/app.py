import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')   # connect with data base 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)
# models is internal representation of model and resource is external representation of model

@app.before_first_request # this decorator run method before the first request (it create data base)
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth
  # add resource in API 
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    
    db.init_app(app)
    app.run(port=5000, debug=True)
