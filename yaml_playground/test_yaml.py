import yaml
from pprint import pprint

if __name__ == '__main__':
    with open('workout.yaml', 'r') as f:
        data = yaml.safe_load(f)
    # The resulting dictionary extends all linked references
    pprint(data)
    pprint(data['program']['schedule'][0])
    pprint(data['program']['schedule'][0]['day']['segments'][0])
