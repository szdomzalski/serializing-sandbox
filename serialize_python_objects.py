import pickle 

data = 255

with open('filename.pkl', 'wb') as f:
    pickle.dump(data, f)

print('Pickle dump of integer 255 (default protocol):')
print(pickle.dumps(data))

for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
    print(f'Protocol v{protocol}: {pickle.dumps(data, protocol)}')