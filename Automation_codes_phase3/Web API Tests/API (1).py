import xmlrpc.client

# The XML-RPC API allows you to interact with Odoo using XML-RPC protocol,
# enabling you to perform CRUD operations on Odoo models

# Connect to Odoo XML-RPC API
url = 'http://localhost:8069'
db = 'your_database_name'
username = 'javaria2912112@gmail.com'
password = 'pakistan555'
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')

# Authenticate and get the user's session ID
uid = common.authenticate(db, username, password, {})

# Create a new record using the create method
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
record_id = models.execute_kw(db, uid, password, 'model_name', 'create', [{
    'field1': 'value1',
    'field2': 'value2',
}])

# Read a record using the read method
record = models.execute_kw(db, uid, password, 'model_name', 'read', [record_id])

# Update a record using the write method
models.execute_kw(db, uid, password, 'model_name', 'write', [[record_id], {
    'field1': 'new_value1',
}])

# Delete a record using the unlink method
models.execute_kw(db, uid, password, 'model_name', 'unlink', [[record_id]])
