import requests


endpoint = "http://localhost:8888/api/products/"

get_response = requests.get(endpoint) 


print(get_response.json())


