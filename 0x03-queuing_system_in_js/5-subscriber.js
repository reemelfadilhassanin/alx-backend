import redis from 'redis';

// Create the Redis client for the subscriber
const subscriber = redis.createClient();

// Event listeners for connection and errors
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Handle messages received on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(message);

  // If the message is "KILL_SERVER", unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
