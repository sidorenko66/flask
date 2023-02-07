import requests

response = requests.get('http://127.0.0.1:5001')
print(response.status_code)
print(response.text)

response = requests.post('http://127.0.0.1:5001',
                         json={'email': 'user1@usermail.ru', 'password': '1234'})
print(response.status_code)
print(response.text)