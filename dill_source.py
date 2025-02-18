from dataclasses import dataclass
import dill

@dataclass
class Person:
    first_name: str
    last_name: str

jdoe = Person('John', 'Doe')

print(jdoe)

dill.dump_module('dill_source.pkl')
