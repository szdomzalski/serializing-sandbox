import requests

response = requests.post('http://localhost:8000/users/', json={"name": "Adam"})
print(response.json())
print(response.status_code)

response = requests.post('http://localhost:8000/users/', json={"name": "Brad"})
print(response.json())
print(response.status_code)

response = requests.get('http://localhost:8000/users/')
print(response.json())
print(response.status_code)

response = requests.post('http://localhost:8000/users/', json={"name": "Charlie"})
print(response.json())
print(response.status_code)

response = requests.get('http://localhost:8000/users/')
print(response.json())
print(response.status_code)