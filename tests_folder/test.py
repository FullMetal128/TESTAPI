import requests

responce = requests.get('https://reqres.in/api/users/2')

print(responce.json())