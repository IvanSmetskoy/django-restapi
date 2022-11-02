import requests


headers = {'Authorization': 'Bearer 3057979ca5fae85d07a30f009af11570f17d8404'}
endpoint = "http://localhost:8888/api/products/"

data = {
    "title": "This is the title for testing API with token",
    "price": 999.99
}

get_response = requests.post(endpoint, json=data, headers=headers) 


print(get_response.json())


