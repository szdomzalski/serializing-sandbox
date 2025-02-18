import dill


def foo(a, b):
    return a + b

print(dill.dumps(foo))

dill.dump(foo, open('dill_function.pkl', 'wb'))