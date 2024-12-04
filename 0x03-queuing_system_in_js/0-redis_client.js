import redis from 'redis';

const client = redis.createClient();  // Create the Redis client

client.on('connect', () => {
  console.log('Redis client connected to the server'); // Success message
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`); // Error message
});
