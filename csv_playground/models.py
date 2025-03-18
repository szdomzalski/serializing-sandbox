import csv
from datetime import datetime
from enum import StrEnum
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

