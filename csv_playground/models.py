import csv
from datetime import datetime
from enum import StrEnum
from pprint import pprint
import random
from typing import NamedTuple

from faker import Faker

class Language(StrEnum):
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"
    IT = "it"
    PL = 'pl'

class User(NamedTuple):
    id: int
    name: str
    email: str
    language: Language
    registered_at: datetime

    # This constructor is generating fake user data for test purposes
    @classmethod
    def fake(cls) -> 'User':
        language = random.choice(list(Language))
        generator = Faker(language)
        return cls(
            generator.pyint(),
            generator.name(),
            generator.email(),
            language,
            generator.date_time_this_year()
        )

    @classmethod
    def from_csv(cls, row: dict) -> 'User':
        return cls(
            int(row['id']),
            row['name'].title(),
            row['email'],
            Language(row['language']),
            datetime.fromisoformat(row['registered_at'])
        )

if __name__ == "__main__":
    HOW_MANY_USERS = 50
    USERS_PATH = '/home/domzalskis/serializing-sandbox/csv_playground/users.csv'
    users = [User.fake() for _ in range(HOW_MANY_USERS)]
    print(users[0])
    # Universal newline translation mechanism should be disabled (avoid issues with portability);
    #   might want to set encoding explicitly too but the default for WSL is utf-8 which is fine in most cases
    with open(USERS_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(users)

    with open(USERS_PATH, 'r', newline='') as f:
        reader = csv.reader(f)  # Default delimiter is comma, reader is an iterator
        read_data_record = next(reader)  # Record is a list, not a named tuple
        print(read_data_record, type(read_data_record))  # Column order is maintained
        for col in read_data_record:
            print(col, type(col))  # All are strings, no matter the original type

    with open(USERS_PATH, 'r', newline='') as f:
        # This won't work well as dict reader does not know the column names;
        #   it would work though if CSV had a header row
        reader = csv.DictReader(f)
        read_data_record = next(reader)
        print(read_data_record, type(read_data_record))
        for key, value in read_data_record.items():
            print(key, value)

    with open(USERS_PATH, 'r', newline='') as f:
        reader = csv.DictReader(f, fieldnames=User._fields)  # This will work well as we provide the column names
        read_data_record = next(reader)
        print(read_data_record, type(read_data_record))  # Dict[str, str]
        for key, value in read_data_record.items():
            print(key, value)

        user_from_csv = User.from_csv(read_data_record)
        print(user_from_csv)

    # Let's try to read all the users
    with open(USERS_PATH, 'r', newline='') as f:
        reader = csv.DictReader(f, fieldnames=User._fields)
        users_from_csv = [User.from_csv(row) for row in reader]
        pprint(users_from_csv[1:10])

