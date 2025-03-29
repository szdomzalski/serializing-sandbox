from users_pb2 import Language as LanguageDAO  # DAO - data access object
from users_pb2 import User as UserDAO
from users_pb2 import Users as UsersDAO

import sys
from pathlib import Path
from pprint import pprint

# Add the parent directory of 'models' to the Python path (otherwise the import will fail)
sys.path.append(str(Path(__file__).resolve().parent.parent / "csv_playground"))

from models import Language
from models import User

if __name__ == "__main__":
    users = [User.fake() for _ in range(5)]

    users_dao = UsersDAO()
    for user in users:
        user_dao = UserDAO()
        user_dao.id = user.id
        user_dao.name = user.name
        user_dao.email = user.email
        user_dao.language = LanguageDAO.Value(user.language.name)
        user_dao.registered_at.FromDatetime(user.registered_at)
        users_dao.users.append(user_dao)

    buffer = users_dao.SerializeToString()  # This in fact returns a bytes object (not a string)
    print(buffer)

    new_users_dao = UsersDAO()
    new_users_dao.ParseFromString(buffer)  # Expecting bytes object as an argument (not a string)
    users = [User(id=user_dao.id,
                  name=user_dao.name,
                  email=user_dao.email,
                  # This is a bit hacky but it works; user_dao.language is an int (index) instead of a string
                  language=list(Language)[user_dao.language],
                  registered_at=user_dao.registered_at.ToDatetime())
             for user_dao in new_users_dao.users]

    pprint(users)