import redis from 'redis';
import { promisify } from 'util';

// Create the Redis client
const client = redis.createClient();

// Promisify the get method to use async/await
const getAsync = promisify(client.get).bind(client);

// Event listeners for connection and errors
client.on('connect', () => {
  console.log('Redis client connected to the server'); // Success message
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`); // Error message
});

// Function to set a new school value in Redis
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print); // Use redis.print to log the response (confirmation)
};

// Function to display the value of a school from Redis using async/await
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);  // Use the promisified client.get
    console.log(value);  // Log the value retrieved from Redis
  } catch (err) {
    console.log(`Error retrieving value for ${schoolName}: ${err}`);
  }
};

// Display the value of 'Holberton' first
displaySchoolValue('Holberton');

// Set a new value for 'HolbertonSanFrancisco'
setNewSchool('HolbertonSanFrancisco', '100');

// Display the value of 'HolbertonSanFrancisco' after setting it
displaySchoolValue('HolbertonSanFrancisco');
