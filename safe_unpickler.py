import importlib
import io
import os
import pickle
from typing import Any

class SafeUnpickler(pickle.Unpickler):
    # Define a whitelist of modules and functions that are allowed to be deserialized
    ALLOWED = {
        "builtins": ["print"],
        "sysconfig": ["get_python_version"],
    }

    # Wraps input bytes sequence into file-like object expected by Unpickler
    @classmethod
    def safe_loads(cls, serialized_data: bytes)-> Any:
        file = io.BytesIO(serialized_data)
        return cls(file).load()

    # Override find_class method to allow only whitelisted modules and functions
    def find_class(self, module_name: str, name: str)-> Any:
        if module_name in self.ALLOWED:
            if name in self.ALLOWED[module_name]:
                module = importlib.import_module(module_name)
                return getattr(module, name)
        raise pickle.UnpicklingError(f"{module_name}.{name} is unsafe")

if __name__ == "__main__":
    # Example usage
    data = pickle.dumps(print)
    print(SafeUnpickler.safe_loads(data))  # Output: <built-in function print>
    data = pickle.dumps(os.system)
    try:
        SafeUnpickler.safe_loads(data)
    except pickle.UnpicklingError as e:
        print(e)  # Output: os.system is unsafe

    try:
        SafeUnpickler.safe_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")  # import os; os.system("echo hello world")
    except pickle.UnpicklingError as e:
        print(e)

    ret = SafeUnpickler.safe_loads(b"csysconfig\nget_python_version\n(tR.")  # import sysconfig; sysconfig.get_python_version()
    print(ret)  # Output: 3.12