import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'Chocolate Milk Bottle',
    'price': 20,
}

get_response = requests.post(endpoint,json=data)
print(get_response.json())