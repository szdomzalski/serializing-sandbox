import bson
import json
from pprint import pprint

if __name__ == "__main__":
    filename = 'workout.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        pprint(data)
        bson_encoded_data = bson.encode(data)
        pprint(bson_encoded_data)
        bson_decoded_data = bson.decode(bson_encoded_data)
        pprint(bson_decoded_data)
        