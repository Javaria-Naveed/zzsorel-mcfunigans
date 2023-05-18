# The XML-RPC ORM API allows you to perform CRUD operations
# on Odoo models using XML-RPC protocol.


import xmlrpc.client
from endpoints import record_id


# Define API endpoint URL
url = 'http://localhost:8069/xmlrpc/2/object'

# Set authentication credentials
db = 'javarias_db'
username = 'javaria2912112@gmail.com'
password = 'pakistan555'

# Create an XML-RPC client
common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

# Create a record
models = xmlrpc.client.ServerProxy(url)
record_id = models.execute_kw(db, uid, password, 'model_name', 'create', [{
    'field1': 'value1',
    'field2': 'value2',
}])

# Read a record
record = models.execute_kw(db, uid, password, 'model_name', 'read', [[record_id]])

# Update a record
models.execute_kw(db, uid, password, 'model_name', 'write', [[record_id], {
    'field1': 'new_value1',
}])

# Delete a record
models.execute_kw(db, uid, password, 'model_name', 'unlink', [[record_id]])
