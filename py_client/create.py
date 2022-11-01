import requests


endpoint = "http://localhost:8888/api/products/"

data = {
    "title": "This is the title for testing API",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data) 


print(get_response.json())


