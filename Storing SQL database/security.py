from hmac import compare_digest
from user import User

# username_mapping={u.username:u for u in users}
# userid_mapping={u.id:u for u in users}



def authenticate(username, password):
    user = User.find_by_username(username)
    if user and compare_digest(user.password, password): # match username and password then generate jwt token
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)