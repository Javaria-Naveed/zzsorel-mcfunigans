import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
  stages: [
    { duration: '3m', target: 20 }, // Ramp-up to 20 virtual users in 3 minutes
    { duration: '5m', target: 20 }, // Stay at 20 virtual users for 5 minutes
    { duration: '2m', target: 0 }, // Ramp-down to 0 virtual users in 2 minutes
  ],
};

export default function () {
  // Send multiple concurrent requests to create records in the Odoo module
  let responses = http.batch([
    ['POST', 'http://localhost:8069/api/create-endpoint', JSON.stringify({ name: 'Record 1', value: 100 })],
    ['POST', 'http://localhost:8069/api/create-endpoint', JSON.stringify({ name: 'Record 2', value: 200 })],
    ['POST', 'http://localhost:8069/api/create-endpoint', JSON.stringify({ name: 'Record 3', value: 300 })],
  ]);

  // Check the response status codes and log the results
  check(responses[0], { 'Status is 201': (r) => r.status === 201 });
  check(responses[1], { 'Status is 201': (r) => r.status === 201 });
  check(responses[2], { 'Status is 201': (r) => r.status === 201 });

  // Pause for 1 second between each virtual user's request
  sleep(1);
}
