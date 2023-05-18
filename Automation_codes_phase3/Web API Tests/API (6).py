import requests
from endpoints import record_id


# Define API endpoint URL
url = 'http://localhost:8069/api/v1'

# Set headers and authentication credentials
headers = {'Content-Type': 'application/json'}
auth = ('javaria2912112@gmail.com', 'pakistan555')

# Perform REST API request to create a record
payload = {
    'field1': 'value1',
    'field2': 'value2',
}
response = requests.post(f'{url}/model_name', json=payload, headers=headers, auth=auth)
created_record = response.json()

# Perform REST API request to retrieve a record
response = requests.get(f'{url}/model_name/{record_id}', headers=headers, auth=auth)
record = response.json()

# Perform REST API request to update a record
payload = {
    'field1': 'new_value1',
}
response = requests.put(f'{url}/model_name/{record_id}', json=payload, headers=headers, auth=auth)

# Perform REST API request to delete a record
response = requests.delete(f'{url}/model_name/{record_id}', headers=headers, auth=auth)
