import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("user: ")
password = getpass()
  
response = requests.get('https://api.github.com/user',
            auth = HTTPBasicAuth(user, password))
  
print(response.text)
print(response)
resposta = response.json()
print(resposta ["name"])

