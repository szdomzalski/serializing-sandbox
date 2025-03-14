import json
import jsonref
from pprint import pprint

if __name__ == "__main__":
    filename = 'workout.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        pprint(data)  # The resulting dictionary does not extend linked references

    with open(filename, 'r') as f:
        data = jsonref.load(f)
        pprint(data)  # Still does not extend linked references - custom logic required to handle @cross-ref
