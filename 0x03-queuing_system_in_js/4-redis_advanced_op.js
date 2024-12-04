import redis from 'redis';

// Create the Redis client
const client = redis.createClient();

// Event listeners for connection and errors
client.on('connect', () => {
  console.log('Redis client connected to the server'); // Success message
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`); // Error message
});

// Function to set hash values for HolbertonSchools
const createHash = () => {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
};

// Function to display the entire hash stored in Redis
const displayHash = () => {
  client.hgetall('HolbertonSchools', (err, object) => {
    if (err) {
      console.log(`Error retrieving hash: ${err}`);
      return;
    }
    console.log(object); // Log the entire hash object
  });
};

// Set the hash values
createHash();

// Display the stored hash after a short delay
setTimeout(displayHash, 1000);
