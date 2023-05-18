import requests
from endpoints import endpoint as ep

#The REST API provides a modern and user-friendly way to interact with Odoo,
# allowing you to perform CRUD operations using HTTP methods (GET, POST, PUT, DELETE).

# Define API endpoint URL
url = f'http://localhost:8069/api/{ep}'

# Set headers and authentication credentials
headers = {'Content-Type': 'application/json'}
auth = ('javaria2912112@gmail.com', 'pakistan555')
record_id='123'

# Perform GET request to retrieve records
response = requests.get(url, headers=headers, auth=auth)
records = response.json()

# Perform POST request to create a record
payload = {
    'field1': 'value1',
    'field2': 'value2',
}
response = requests.post(url, json=payload, headers=headers, auth=auth)
created_record = response.json()

# Perform PUT request to update a record
update_url = f'{url}/{record_id}'
updated_payload = {
    'field1': 'new_value1',
}
response = requests.put(update_url, json=updated_payload, headers=headers, auth=auth)

# Perform DELETE request to delete a record
delete_url = f'{url}/{record_id}'
response = requests.delete(delete_url, headers=headers, auth=auth)
