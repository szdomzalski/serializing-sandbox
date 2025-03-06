import requests

response = requests.get('http://localhost:8000/users')
print(response.json())
print(response.status_code)

response = requests.post('http://localhost:8000/users', json={"name": "Charlie"})
print(response.json())
print(response.status_code)

response = requests.get('http://localhost:8000/users')
print(response.json())
print(response.status_code)