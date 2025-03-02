import jsonpickle

from customize_pickle import User

user = User(name="John Doe", password="secret")
user_json = jsonpickle.dumps(user, indent=4)  # encode
print(user_json)

user_retrieved = jsonpickle.loads(user_json)  # decode
print(user_retrieved)