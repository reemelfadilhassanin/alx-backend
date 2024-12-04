const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

// Create Redis client and promisify methods
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Create Kue queue
const queue = kue.createQueue();

// Initial setup
let reservationEnabled = true;
const initialSeats = 50;
client.set('available_seats', initialSeats);

// Reserve seat function in Redis
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Get current available seats
async function getCurrentAvailableSeats() {
  return parseInt(await getAsync('available_seats')) || 0;
}

const app = express();
const port = 1245;

// Route to check available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats.toString() });
});

// Route to reserve seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservation are blocked" });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: "Reservation failed" });
    }
    res.json({ status: "Reservation in process" });
  });
});

// Route to process reservation queue
app.get('/process', async (req, res) => {
  res.json({ status: "Queue processing" });

  const availableSeats = await getCurrentAvailableSeats();

  if (availableSeats > 0) {
    const job = queue.process('reserve_seat', async (job, done) => {
      const newAvailableSeats = availableSeats - 1;
      await reserveSeat(newAvailableSeats);
      
      if (newAvailableSeats === 0) {
        reservationEnabled = false;
      }

      console.log(`Seat reservation job ${job.id} completed`);
      done();
    });
  } else {
    queue.failed('reserve_seat', new Error('Not enough seats available'));
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

