import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  vus: 50, // 50 virtual users
  duration: '5m', // Run the test for 5 minutes
};

export default function () {
  // Perform an HTTP POST request to authenticate a user in the Odoo module
  let payload = JSON.stringify({ username: 'user1', password: 'password123' });
  let headers = { 'Content-Type': 'application/json' };
  let response = http.post('http://localhost:8069/api/authenticate-endpoint', payload, { headers });

  // Check the response status code and log the result
  check(response, { 'Status is 200': (r) => r.status === 200 });

  // Pause for 2 seconds between each virtual user's request
  sleep(2);
}
