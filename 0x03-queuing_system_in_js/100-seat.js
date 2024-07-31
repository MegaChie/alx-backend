const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

const app = express();
const port = 1245;

const client = redis.createClient();

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

(async () => {
  await reserveSeat(50);
})();

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', async () => {
    const seats = await getCurrentAvailableSeats();

    if (seats > 0) {
      await reserveSeat(seats - 1);
      console.log(`Seat reservation job ${job.id} completed`);
    } else {
      reservationEnabled = false;
      console.log(`Seat reservation job ${job.id} completed, but no seats left`);
    }
  }).on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
