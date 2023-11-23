import requests

endpoint = "http://localhost:8000/api"
#endpoint = "https://httpbin.com/anything"

get_response = requests.get(endpoint, params={"abc": 123}, json={"message": "Hello"})
print(get_response.json())