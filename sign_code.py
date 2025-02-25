import hashlib
import hmac
from pathlib import Path
import dill
from typing import Any, BinaryIO, Callable


def safe_dump(obj: Any, file: BinaryIO, key: str, algorithm: Callable = hashlib.sha256) -> None:
    serialized_data = dill.dumps(obj)
    signature = hmac.new(key.encode(), serialized_data, algorithm).digest()
    dill.dump(signature, file)
    file.write(serialized_data)

def safe_load(file: BinaryIO, key: str, algorithm: Callable = hashlib.sha256) -> Any:
    signature = dill.load(file)
    serialized_data = file.read()
    if signature != hmac.new(key.encode(), serialized_data, algorithm).digest():
        raise dill.UnpicklingError("Signature mismatch")
    return dill.loads(serialized_data)


if __name__ == "__main__":
    path = Path("code.pkl")
    code = lambda x, y: x + y

    with path.open("wb") as file:
        safe_dump(code, file, "my_secret_key")
        print(code)
        print(code(1, 2))

    with path.open("rb") as file:
        loaded_code = safe_load(file, "my_secret_key")
        print(loaded_code)
        print(loaded_code(1, 2))
        print(loaded_code == code)
        print(id(loaded_code) == id(code))

    with path.open("rb") as file:
        try:
            safe_load(file, "wrong_key")
        except dill.UnpicklingError as e:
            print(e)