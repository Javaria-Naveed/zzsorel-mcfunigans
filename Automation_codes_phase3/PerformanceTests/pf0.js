import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 50 }, // Ramp-up to 50 virtual users in 1 minute
    { duration: '5m', target: 50 }, // Stay at 50 virtual users for 5 minutes
    { duration: '1m', target: 0 }, // Ramp-down to 0 virtual users in 1 minute
  ],
};

export default function () {
  // Perform an HTTP POST request to create a record in the Odoo module
  let payload = JSON.stringify({ name: 'Test Record', value: 100 });
  let headers = { 'Content-Type': 'application/json' };
  let response = http.post('http://localhost:8069/api/create-endpoint', payload, { headers });

  // Check the response status code and log the result
  if (response.status === 201) {
    console.log('Record created successfully');
  } else {
    console.log(`Failed to create record with status code ${response.status}`);
  }

  // Pause for 2 seconds between each virtual user's request
  sleep(2);
}

//In this example, the K6 script includes stages to simulate a ramp-up of 50 virtual users, a steady load of 50 virtual users,
//and a ramp-down to 0 virtual users over specific durations. The http.post function is used to send an HTTP POST request to create
//a record in the Odoo module. Adjust the URL ('http://localhost:8069/api/create-endpoint') and payload as per your specific module's API endpoint.