import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 100, // 100 virtual users
  duration: '5m', // Run the test for 5 minutes
};

export default function () {
  // Perform an HTTP GET request to retrieve records from the Odoo module
  let response = http.get('http://localhost:8069/api/records-endpoint');

  // Check the response status code and log the result
  if (response.status === 200) {
    console.log('Records retrieved successfully');
  } else {
    console.log(`Failed to retrieve records with status code ${response.status}`);
  }

  // Pause for 1 second between each virtual user's request
  sleep(1);
}
