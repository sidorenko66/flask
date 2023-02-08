import requests

response = requests.post('http://127.0.0.1:5001/users',
                         json={'email': 'user1@usermail.ru', 'password': '1234'})
print(response.status_code)
print(response.text)

response = requests.get('http://127.0.0.1:5001/users/1')
print(response.status_code)
print(response.text)

response = requests.post('http://127.0.0.1:5001/ads',
                         json={'title': 'new ad 1', 'description': 'some description', 'user_id': 1})
print(response.status_code)
print(response.text)

response = requests.get('http://127.0.0.1:5001/ads/1')
print(response.status_code)
print(response.text)

response = requests.patch('http://127.0.0.1:5001/ads/1',
                         json={'title': 'new ad 1 patch', 'description': 'some description patch', 'user_id': 1})
print(response.status_code)
print(response.text)

response = requests.get('http://127.0.0.1:5001/ads/1')
print(response.status_code)
print(response.text)

response = requests.delete('http://127.0.0.1:5001/ads/1')
print(response.status_code)
print(response.text)

response = requests.get('http://127.0.0.1:5001/ads/1')
print(response.status_code)
print(response.text)
