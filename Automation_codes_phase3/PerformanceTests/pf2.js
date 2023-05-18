import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 50 }, // Ramp-up to 50 virtual users in 2 minutes
    { duration: '10m', target: 50 }, // Stay at 50 virtual users for 10 minutes
    { duration: '2m', target: 0 }, // Ramp-down to 0 virtual users in 2 minutes
  ],
};

export default function () {
  // Perform an HTTP PUT request to update a record in the Odoo module
  let payload = JSON.stringify({ id: 123, name: 'Updated Record', value: 200 });
  let headers = { 'Content-Type': 'application/json' };
  let response = http.put('http://localhost:8069/api/update-endpoint', payload, { headers });

  // Check the response status code and log the result
  if (response.status === 200) {
    console.log('Record updated successfully');
  } else {
    console.log(`Failed to update record with status code ${response.status}`);
  }

  // Pause for 3 seconds between each virtual user's request
  sleep(3);
}
