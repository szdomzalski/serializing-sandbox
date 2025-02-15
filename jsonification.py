import json

from numpy import mat

data = {
    "email": None,
    "name": "John Doe",
    "age": 42.5,
    "married": True,
    "children": ["Alice", "Bob"],
}

print(json.dumps(data, indent=4, sort_keys=True))

def serialize_set(value: set) -> str:
    return {"type": "set", "elements": list(value)}

data = {'weekend days': {'Saturday', 'Sunday'}}
jsonified_set = json.dumps(data, default=serialize_set, indent=4, sort_keys=True)
print(jsonified_set)

deserialized_set = json.loads(jsonified_set)
print(deserialized_set)  # {'weekend days': {'type': 'set', 'elements': ['Saturday', 'Sunday']}}

def deserialize_set(dct: dict) -> set:
    match dct:
        case {"type": "set", "elements": list_elements}:
            return set(list_elements)
    # if dct.get("type") == "set":
    #     return set(dct["elements"])
    return dct

deserialized_set = json.loads(jsonified_set, object_hook=deserialize_set)
print(deserialized_set)  # {'weekend days': {'Saturday', 'Sunday'}}
