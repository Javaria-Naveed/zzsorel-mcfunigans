import requests
from endpoints import record_id


# Define API endpoint URL
url = 'http://localhost:8069/jsonrpc'

# Set headers and authentication credentials
headers = {'Content-Type': 'application/json'}
auth = ('your_username', 'your_password')

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

# Perform JSON-RPC request to retrieve a record
payload = {
    'jsonrpc': '2.0',
    'method': 'call',
    'params': {
        'model': 'model_name',
        'method': 'read',
        'args': [[record_id], ['field1', 'field2']],
    },
    'id': 2,
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
    'id': 3,
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
    'id': 4,
}
response = requests.post(url, json=payload, headers=headers, auth=auth)
