import pickle 
import sys

data = 255
PICKLED_DATAFILE = 'filename.pkl'

with open(PICKLED_DATAFILE, 'wb') as f:
    pickle.dump(data, f)

print('Pickle dump of integer 255 (default protocol):')
print(pickle.dumps(data))

pickle_protocol_results = []
for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
    pickle_protocol_results.append(pickle.dumps(data, protocol))    
    print(f'Protocol v{protocol}: {pickle.dumps(data, protocol)}')

with open(PICKLED_DATAFILE, 'rb') as f:
    read_data = pickle.load(f)

print(read_data, data)
print(type(read_data), type(data))

for protocol, result in enumerate(pickle_protocol_results):
    print(f'Protocol v{protocol}: {pickle.loads(result)}')

cycle_example = {}
cycle_example['sibling'] = {'sibling': cycle_example}
cycle_dump = pickle.dumps(cycle_example)
print(cycle_dump)
cycle_retrieved = pickle.loads(cycle_dump)
print(cycle_retrieved)

recursive_example = []
recursive_example.append(recursive_example)
recursive_dump = pickle.dumps(recursive_example)
print(recursive_dump)
recursive_retrieved = pickle.loads(recursive_dump)
print(recursive_retrieved)

deep_nested = []
for _ in range(sys.getrecursionlimit() // 2):
    deep_nested = [deep_nested]

deep_nested_dump = pickle.dumps(deep_nested)
print(deep_nested_dump)
deep_nested_retrieved = pickle.loads(deep_nested_dump)
print(deep_nested_retrieved)