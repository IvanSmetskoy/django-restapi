import requests


endpoint = "http://localhost:8888/api/products/1/update/"


data = {
    "title": "XXXXXXXXXXX",
    "price": 0.01
}


get_response = requests.put(endpoint, json=data) 


print(get_response.json())


