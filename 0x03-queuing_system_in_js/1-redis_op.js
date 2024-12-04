import redis from 'redis';

const client = redis.createClient();  // Create the Redis client

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

// Function to display the value of a school from Redis
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error retrieving value for ${schoolName}: ${err}`);
    } else {
      console.log(reply); // Log the retrieved value for the given school name
    }
  });
};

// Display the value of 'Holberton' first
displaySchoolValue('Holberton');

// Set a new value for 'HolbertonSanFrancisco'
setNewSchool('HolbertonSanFrancisco', '100');

// Display the value of 'HolbertonSanFrancisco' after setting it
displaySchoolValue('HolbertonSanFrancisco');
