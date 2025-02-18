import dill

foo = dill.load(open('dill_function.pkl', 'rb'))

print(foo)
print(foo(1, 2))