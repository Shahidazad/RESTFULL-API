from hmac import compare_digest # campare same string
from user import User

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and compare_digest(user.password, password): # campare same string
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)