import hashlib
import hmac
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