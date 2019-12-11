import shelve

class User:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.name = ''
        self.email = ''

def clear_user():
    user_db = shelve.open('user')
    for key in user_db:
        del user_db[key]
    user_db.close()

def get_users():
    user_list = []
    user_db = shelve.open('user')
    for key in user_db:
        user_list.append(user_db[key])
    user_db.close()
    return user_list

def init_users():
    clear_user()
    for i in range(1,6):
        create_user('user'+str(i), 'pass'+str(i), 'test user'+str(i), 'user'+str(i)+'@mail.com')

def get_user(username, password):
    user_db = shelve.open('user')
    user = None
    if username in user_db:
        if user_db[username].password == password:
            user = user_db[username]
    user_db.close()
    return user

def create_user(username, password, name, email):
    user_db = shelve.open('user')
    u = User()
    u.username = username
    u.password = password
    u.name = name
    u.email = email
    user_db[username] = u
    user_db.close()



