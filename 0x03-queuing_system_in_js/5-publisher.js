import redis from 'redis';

// Create the Redis client for the publisher
const publisher = redis.createClient();

// Event listeners for connection and errors
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Function to publish a message after a delay
const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message); // Publish the message
  }, time);
};

// Call the function to publish messages with different delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
