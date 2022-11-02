import requests
from getpass import getpass


auth_endpoint = "http://localhost:8888/api/auth/"
username = input("Enter your username:\n")
password = getpass("Enter your password:\n")

auth_response = requests.post(auth_endpoint, json={'username': username, "password": password}) 
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8888/api/products/"

    get_response = requests.get(endpoint, headers=headers) 
    print(get_response.json())


