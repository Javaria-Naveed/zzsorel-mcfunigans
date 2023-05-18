# Odoo webhooks allow you to receive real-time notifications about specific
# events or changes in the system, such as record creation, update, deletion, etc

from flask import Flask, request
from endpoints import record_id

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Parse the incoming webhook payload
    payload = request.json

    # Process the payload and perform necessary actions
    event_type = payload.get('event_type')
    if event_type == 'record_created':
        # Handle record creation event
        record_id = payload.get('record_id')
        # Perform desired actions for record creation

    elif event_type == 'record_updated':
        # Handle record update event
        record_id = payload.get('record_id')
        # Perform desired actions for record update

    elif event_type == 'record_deleted':
        # Handle record deletion event
        record_id = payload.get('record_id')
        # Perform desired actions for record deletion

    # Return a response to the webhook sender
    return 'Webhook received and processed successfully'

if __name__ == '__main__':
    app.run()

