# The JSON-RPC API is an alternative to the XML-RPC API and allows you to perform
# CRUD operations on Odoo models using JSON-RPC protocol.

import requests
from endpoints import record_id

# Define API endpoint URL
url = 'http://localhost:8069/jsonrpc'

# Set headers and authentication credentials
headers = {'Content-Type': 'application/json'}
auth = ('javaria2912112@gmail.com', 'pakistan555')

# Perform JSON-RPC request to create a record
payload = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'model': 'model_name',
        'method': 'create',
        'args': [{
            'field1': 'value1',
            'field2': 'value2',
        }],
    },
    'id': 1,
}
response = requests.post(url, json=payload, headers=headers, auth=auth)
created_record = response.json()['result']

# Perform JSON-RPC request to read a record
payload = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'model': 'model_name',
        'method': 'read',
        'args': [[record_id]],
    },
    'id': 1,
}
response = requests.post(url, json=payload, headers=headers, auth=auth)
record = response.json()['result']

# Perform JSON-RPC request to update a record
payload = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'model': 'model_name',
        'method': 'write',
        'args': [[record_id], {
            'field1': 'new_value1',
        }],
    },
    'id': 1,
}
response = requests.post(url, json=payload, headers=headers, auth=auth)

# Perform JSON-RPC request to delete a record
payload = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'model': 'model_name',
        'method': 'unlink',
        'args': [[record_id]],
    },
    'id': 1,
}
response = requests.post(url, json=payload, headers=headers, auth=auth)
