import importlib
import inspect


def get_module_source(module_name):
     module = importlib.import_module(module_name)
     return inspect.getsource(module)

source_code = get_module_source('pickle_code')
print(source_code)

exec(source_code)
print(plus_one(3))