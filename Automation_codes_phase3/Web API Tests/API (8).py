# The Web Controller API allows you to define custom web controllers in
# Odoo to handle specific routes and HTTP requests.

import requests

# Define API endpoint URL
url = 'http://localhost:8069/custom_controller_route'

# Set headers and authentication credentials if required
headers = {'Content-Type': 'application/json'}
auth = ('javaria2912112@gmail.com', 'pakistan555')

# Perform HTTP request to the custom web controller
response = requests.get(url, headers=headers, auth=auth)

# Process the response
data = response.json()
