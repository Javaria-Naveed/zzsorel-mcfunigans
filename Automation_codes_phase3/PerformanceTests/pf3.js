import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 50, // 50 virtual users
  duration: '10m', // Run the test for 10 minutes
};

export default function () {
  // Perform an HTTP DELETE request to delete a record in the Odoo module
  let response = http.del('http://localhost:8069/api/delete-endpoint?id=123');

  // Check the response status code and log the result
  if (response.status === 204) {
    console.log('Record deleted successfully');
  } else {
    console.log(`Failed to delete record with status code ${response.status}`);
  }

  // Pause for 2 seconds between each virtual user's request
  sleep(2);
}
