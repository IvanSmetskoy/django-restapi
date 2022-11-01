import requests

#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8888/api/"

get_response = requests.post(endpoint, json={"title": "Title 1", "content": "Hello World^^^", "price": 99.99}) # HTTP GET request
#print(get_response.headers)
#print(get_response.text)
#print(get_response.status_code)

print(get_response.json())
#print(get_response.status_code)

