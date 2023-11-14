import requests

product_id = input('What id do you want to delete?: ')

try:
    product_id = int(product_id)
except:
    print(f'The id {product_id} is not valid!')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)