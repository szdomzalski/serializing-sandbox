import pickle

def create_plus(x):
    def plus(y):
        return x + y

    return plus

if __name__ == "__main__":
    plus_one = create_plus(1)


    try:
        print(pickle.dumps(plus_one))  # Fail, inner functions cannot be pickled as these are locals
    except AttributeError as e:
        print(e)

    try:
        print(pickle.dumps(lambda x: x + 2))  # Fail, lambda functions cannot be pickled as these are anonymous
    except pickle.PickleError as e:
        print(e)

    try:
        print(pickle.dumps(create_plus))  # Success, create_plus is a global function
    except AttributeError as e:
        print(e)

    unpickled_create_plus = pickle.loads(pickle.dumps(create_plus))

    print(unpickled_create_plus(2)(3))  # 5